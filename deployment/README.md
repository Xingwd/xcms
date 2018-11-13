# 安装基础依赖
```
sudo apt-get -y update
sudo apt-get -y install python3 python3-venv python3-dev
sudo apt-get -y install mysql-server libmysqlclient-dev supervisor nginx git
```

# (可选)部署Elasticsearch
参考：[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/docker.html)

该小节提供Elasticsearch开发模式的启动说明，本应用可使用Elasticsearch作为全文搜索引擎，如果不想使用Elasticsearch，可跳过这一步。

如果要使用Elasticsearch引擎，请务必在一开始使用，不要在应用运行中途使用，因为Elasticsearch索引信息需要和数据库信息保持同步。

> Elasticsearch生产模式要求机器内存不低于2G。
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:6.4.3
docker run -d --name es -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.4.3
```
停止和启动es
```
docker stop es
docker start es
```

# 安装应用
```
cd /var/www/
git clone https://github.com/Xingwd/xcms.git
cd xcms
git checkout v0.2.0
```


# 设置Mysql
## 创建数据库
```
create database xcms character set utf8 collate utf8_bin;
create user '<db-user>'@'localhost' identified by '<db-password>';
grant all privileges on xcms.* to '<db-user>'@'localhost';
flush privileges;
quit;
```

# 设置环境变量
为SECRET_KEY生成一个随机字符串：
```
python3 -c "import uuid; print(uuid.uuid4().hex)"
```

创建`/var/www/xcms/.env`文件，添加内容(替换相应信息)：
```
SECRET_KEY=random string
DATABASE_URL=mysql://<db-user>:<db-password>@localhost/xcms
```

(可选)激活Elasticsearch，向`.env`文件添加如下配置：
```
ELASTICSEARCH_URL=http://localhost:9200
```


创建`/etc/profile.d/xcms.sh`文件，添加内容：
```
# xcms env
export FLASK_APP=/var/www/xcms/xcms.py
```

重载环境变量
```
source /etc/profile
```


# 创建Python虚拟环境
(pip清华源：https://pypi.tuna.tsinghua.edu.cn/simple)
```
cd /var/www/xcms
python3 -m venv venv
source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
(venv) $ pip install gunicorn
```

# 初始化数据库
```
flask db upgrade
```

# 创建管理员账户
```
flask createadmin --name <admin-user> --password <admin-password>
```

# 设置Gunicorn和Supervisor
编辑`/etc/supervisor/conf.d/xcms.conf`文件：
```
[program:xcms]
command=/var/www/xcms/venv/bin/gunicorn -b localhost:8000 -w 4 xcms:app
directory=/var/www/xcms
user=root
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```

重载服务
```
sudo supervisorctl reload
```

# 设置Nginx
## 设置自签名SSL证书
使用自签名SSL证书，网站将会被标记为不可信，自签名SSL证书用于测试，生产环境请使用第三方机构SSL证书，在下面的环节将会介绍免费的第三方SSL证书如何使用。
```
cd /var/www/
mkdir certs
openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
  -keyout certs/key.pem -out certs/cert.pem
```
该命令将要求你提供关于应用程序和你自己的一些信息。这些信息将包含在SSL证书中，如果用户请求查看它，Web浏览器则会向用户显示它们。上述命令的结果将是名为key.pem和cert.pem的两个文件，存放在certs目录下。

## 创建nginx配置文件
编辑`/etc/nginx/sites-enabled/xcms`文件：
```
server {
    # listen on port 80 (http)
    listen 80;
    server_name xingweidong.com www.xingweidong.com;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name xingweidong.com www.xingweidong.com;

    # location of the self-signed SSL certificate
    ssl_certificate /var/www/certs/cert.pem;
    ssl_certificate_key /var/www/certs/key.pem;

    # write access and error logs to /var/log
    access_log /var/log/xcms_access.log;
    error_log /var/log/xcms_error.log;

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://localhost:8000;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        # handle static files directly, without forwarding to the application
        alias /var/www/xcms/app/static;
        expires 30d;
    }
}
```

重载配置
```
sudo service nginx reload
```


## 使用第三方SSL证书
使用 [Let's Encrypt](https://letsencrypt.org/getting-started/) 免费SSL证书

### 安装[Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx)
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
```

### 生成证书
```
sudo certbot --nginx certonly
```
> 使用certonly子命令，可以手动编辑Nginx配置，否则Certbot也将自动生成Nginx配置

完成后，输入信息提示，证书和key文件保存路径：
```
/etc/letsencrypt/live/xingweidong.com/fullchain.pem
/etc/letsencrypt/live/xingweidong.com/privkey.pem
```

### 自动续延
```
sudo certbot renew --dry-run
```

### 更新nginx配置文件
编辑`/etc/nginx/sites-enabled/xcms`文件：
```
server {
    # listen on port 80 (http)
    listen 80;
    server_name xingweidong.com www.xingweidong.com;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name xingweidong.com www.xingweidong.com;

    # location of the self-signed SSL certificate
    ssl_certificate /etc/letsencrypt/live/xingweidong.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/xingweidong.com/privkey.pem;

    # write access and error logs to /var/log
    access_log /var/log/xcms_access.log;
    error_log /var/log/xcms_error.log;

    location / {
        # forward application requests to the gunicorn server
        proxy_pass http://localhost:8000;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        # handle static files directly, without forwarding to the application
        alias /var/www/xcms/app/static;
        expires 30d;
    }
}
```

重载配置
```
sudo service nginx reload
```

# 应用更新
```
(venv) $ git pull                           # download the new version
(venv) $ sudo supervisorctl stop xcms       # stop the current server
(venv) $ flask db upgrade                   # upgrade the database
(venv) $ sudo supervisorctl start xcms      # start a new server
```
