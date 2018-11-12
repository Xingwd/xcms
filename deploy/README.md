# 安装基础依赖
```
sudo apt-get -y update
sudo apt-get -y install python3.6 python3.6-venv python3.6-dev
sudo apt-get -y install mysql-server supervisor nginx git
```

# 部署Elasticsearch(开发模式)
参考：[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/docker.html)

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
git clone https://github.com/Xingwd/xcms.git
cd xcms
git checkout v0.1.0
```

# 设置环境变量
为SECRET_KEY生成一个随机字符串：
```
python3 -c "import uuid; print(uuid.uuid4().hex)
```

编辑`~/.profile`文件，追加内容(替换相应内容)：
```
# xcms env
export SECRET_KEY="random string"
export DATABASE_URL="mysql://<db-user>:<db-password>@localhost/xcms"
export ELASTICSEARCH_URL="http://localhost:9200"
export FLASK_APP=xcms.py
```

重载环境变量
```
source ~/.profile
```


# 创建Python虚拟环境
(pip国内源：https://pypi.tuna.tsinghua.edu.cn/simple)
```
python3 -m venv venv
source venv/bin/activate
(venv) $ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
(venv) $ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gunicorn mysql-client
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

## 初始化数据库
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
command=/home/ubuntu/xcms/venv/bin/gunicorn -b localhost:8000 -w 4 xcms:app
directory=/home/ubuntu/xcms
user=ubuntu
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
编辑`/etc/nginx/sites-enabled/xcms`文件：
```
server {
    # listen on port 80 (http)
    listen 80;
    server_name _;
    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}
server {
    # listen on port 443 (https)
    listen 443 ssl;
    server_name _;

    # location of the self-signed SSL certificate
    ssl_certificate /home/ubuntu/certs/cert.pem;
    ssl_certificate_key /home/ubuntu/certs/key.pem;

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
        alias /home/ubuntu/xcms/static;
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
(venv) $ git pull                              # download the new version
(venv) $ sudo supervisorctl stop xcms          # stop the current server
(venv) $ flask db upgrade                      # upgrade the database
(venv) $ sudo supervisorctl start xcms         # start a new server
```