# XCMS

使用MVVM架构

后端server使用Flask，提供Restful API

前端admin使用 Vue + Element

前端web使用 Vue + Vuetify


# 部署
> 操作系统CentOS7

## 准备
### 安装基础服务
> 数据库使用mariadb
```
yum install git nginx supervisor mariadb-server mariadb-devel
```

### 安装基础环境
#### Nodejs
下载 [Linux x64 tar](https://npm.taobao.org/mirrors/node/v12.14.1/node-v12.14.1-linux-x64.tar.xz)。

解压后，配置环境变量即可。
#### Pyenv
参照 [安装说明](https://github.com/pyenv/pyenv#installation) 进行安装。


### 获取应用代码
```
mkdir /var/www
cd /var/www
git clone https://github.com/Xingwd/xcms.git
cd xcms
git checkout v1.0.0
```


## server
### 创建Python虚拟环境
> pip清华源：https://pypi.tuna.tsinghua.edu.cn/simple

```
pyenv install 3.7.6
/root/.pyenv/versions/3.7.6/bin/pip install virtualenv
cd /var/www/xcms/server
/root/.pyenv/versions/3.7.6/bin/virtualenv venv
venv/bin/pip install -r requirements.txt
venv/bin/pip install uwsgi
venv/bin/pip install mysqlclient
```

### 应用基础设置
#### 数据库设置
```
create database xcms character set utf8 collate utf8_bin;
create user '<db-user>'@'localhost' identified by '<db-password>';
grant all privileges on xcms.* to '<db-user>'@'localhost';
flush privileges;
quit;
```
#### 应用生产配置
为SECRET_KEY生成一个随机字符串：
```
cd /var/www/xcms/server
venv/bin/python -c "import uuid; print(uuid.uuid4().hex)"
```
编辑`/var/www/xcms/server/.env`：
```
SECRET_KEY=<random string>
SQLALCHEMY_DATABASE_URI=mysql://<db-user>:<db-password>@localhost/xcms
```
#### 初始化应用模型
```
source venv/bin/activate
export FLASK_APP=/var/www/xcms/server/xcms.py
flask db upgrade
```
#### 创建管理员用户
```
flask createadmin --name <admin-user> --password <admin-password>
```

### 设置Supervisor
编辑/etc/supervisord.d/xcms.ini文件：
```
[program:xcms]
command=/var/www/xcms/server/venv/bin/uwsgi --http-socket 127.0.0.1:3031 --wsgi-file xcms.py --callable app --processes 2 --threads 2 --stats 127.0.0.1:9191
directory=/var/www/xcms/server
user=root
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```
重载supervisor服务：`supervisorctl reload`


## admin
编译
```
cd xcms/amdin
npm run build
```
结果目录`admin/dist`。


## web
编译
```
cd xcms/web
npm run build
```
结果目录`web/dist`。


## 设置Nginx
### 安装第三方SSL证书
使用 [Let's Encrypt](https://letsencrypt.org/getting-started/) 免费SSL证书

[CentOS7安装Certbot](https://certbot.eff.org/lets-encrypt/centosrhel7-nginx)

### Nginx配置文件
编辑`/etc/nginx/nginx.conf`文件，主要修改：
```
http {
    ...

    server {
        listen       80;
        server_name xingweidong.com www.xingweidong.com;

        ...

        location / {
            # redirect any requests to the same URL but on https
            return 301 https://$host$request_uri;
        }

        ...
    }

    # HTTPS server
    #
    server {
        listen       443 ssl;
        server_name xingweidong.com www.xingweidong.com;

        ssl_certificate /etc/letsencrypt/live/xingweidong.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/xingweidong.com/privkey.pem;

        ...

        # write access and error logs to /var/log
        access_log /var/log/xcms_access.log;
        error_log /var/log/xcms_error.log;

        location /server {
            proxy_pass http://127.0.0.1:3031;
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        location /admin {
            alias /var/www/xcms/admin/dist/;
        }

        location / {
            alias /var/www/xcms/web/dist/;
        }
    }
}
```

重载nginx：`systemctl reload nginx`

开始启动后，服务无法正常运行，观察`/var/log/nginx/error.log`发现问题：
```
connect() to 127.0.0.1:3031 failed (13: Permission denied) while connecting to upstream
```
网上查阅资料后，解决方案是执行以下命令：(以后有时间再细究)
```
setsebool -P httpd_can_network_connect 1
```
