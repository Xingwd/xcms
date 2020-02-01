# XCMS

使用MVVM架构

后端server使用Flask，提供Restful API

前端admin使用 Vue + Element

前端web使用 Vue + Vuetify


# 部署
> 操作系统CentOS7

## 准备
安装基础服务和环境：mysql(or mariadb), nginx, supervisor, git, nodejs, pyenv

获取应用代码
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
```

### 应用基础设置
**数据库设置**
```
create database xcms character set utf8 collate utf8_bin;
create user '<db-user>'@'localhost' identified by '<db-password>';
grant all privileges on xcms.* to '<db-user>'@'localhost';
flush privileges;
quit;
```
**初始化应用模型**
```
source venv/bin/activate
flask db upgrade
```
**创建管理员用户**
```
flask createadmin --name <admin-user> --password <admin-password>
```

### 设置Supervisor
编辑/etc/supervisor/conf.d/xcms.conf文件：
```
[program:xcms]
command=/var/www/xcms/venv/bin/uwsgi --socket 127.0.0.1:3031 --wsgi-file xcms.py --callable app --processes 2 --threads 2 --stats 127.0.0.1:9191
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
```
cd /etc/nginx
cp nginx.conf.default conf.d/xcms.conf
```

主要修改：
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

        location /xcms {
            include uwsgi_params;
            uwsgi_pass 127.0.0.1:3031/xcms;
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
