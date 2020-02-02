# XCMS

使用MVVM架构

后端server使用Flask，提供Restful API

前端admin使用 Vue + Element

前端web使用 Vue + Vuetify


# 编译
## 安装Nodejs
下载 [Linux x64 tar](https://npm.taobao.org/mirrors/node/v12.14.1/node-v12.14.1-linux-x64.tar.xz)。

解压后，配置环境变量即可。

配置淘宝镜像：`npm config set registry http://registry.npm.taobao.org/`

安装Vue CLI：`npm install -g @vue/cli`


## 获取应用代码
```
git clone https://github.com/Xingwd/xcms.git
cd xcms
```
切换release tag分支：(以 v1.0.0 为例)
```
git checkout v1.0.0
```

## 编译admin
```
cd xcms/amdin
npm install
npm run build
```
结果目录`admin/dist`。

## 编译web
```
cd xcms/web
npm install
npm run build
```
结果目录`web/dist`。

## 打包工程
编译完成后，将整个工程打包，打包命令如下：
```
tar czvf xcms.tar.gz xcms
```


# 部署
> 操作系统Ubuntu18.04

选择要部署的版本，按照上面的编译步骤进行编译，然后上传工程编译结果：
```
scp xcms.tar.gz root@xcms:/root/
```

## 准备
### 解压工程
```
mkdir /var/www/
tar zxvf xcms.tar.gz -C /var/www/
```

### 安装基础服务
> 数据库使用mysql

```
sudo apt-get install git nginx supervisor mysql-server libmysqlclient-dev
```

### 安装Pyenv
> 注意第5步：Install Python build dependencies

参照 [安装说明](https://github.com/pyenv/pyenv#installation) 进行安装。


## 创建Python虚拟环境
> pip清华源使用帮助：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

```
pyenv install 3.7.6
/root/.pyenv/versions/3.7.6/bin/pip install virtualenv
mkdir /opt/pyvenv
cd /opt/pyvenv
/root/.pyenv/versions/3.7.6/bin/virtualenv xcms
xcms/bin/pip install -r /var/www/xcms/server/requirements.txt
xcms/bin/pip install uwsgi
xcms/bin/pip install mysqlclient
```

## 数据库设置
```
create database xcms character set utf8 collate utf8_bin;
create user '<db-user>'@'localhost' identified by '<db-password>';
grant all privileges on xcms.* to '<db-user>'@'localhost';
flush privileges;
quit;
```
## 应用生产配置
为SECRET_KEY生成一个随机字符串：
```
python -c "import uuid; print(uuid.uuid4().hex)"
```
编辑`/var/www/xcms/server/.env`：
```
SECRET_KEY=<random string>
SQLALCHEMY_DATABASE_URI=mysql://<db-user>:<db-password>@localhost/xcms
```
### 初始化应用模型
```
source /opt/pyvenv/xcms/bin/activate
export FLASK_APP=/var/www/xcms/server/xcms.py
flask db upgrade
```
### 创建管理员用户
```
flask createadmin --name <admin-user> --password <admin-password>
```

## 设置Supervisor
编辑/etc/supervisor/conf.d/xcms.conf文件：
```
[program:xcms]
command=/opt/pyvenv/xcms/bin/uwsgi --http-socket 127.0.0.1:3031 --wsgi-file xcms.py --callable app --processes 2 --threads 2 --stats 127.0.0.1:9191
directory=/var/www/xcms/server
user=root
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
```
重载supervisor服务：`supervisorctl reload`

## 设置Nginx
### 安装第三方SSL证书
使用 [Let's Encrypt](https://letsencrypt.org/getting-started/) 免费SSL证书

[Ubuntu18安装Certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx)

### Nginx配置文件
编辑`/etc/nginx/conf.d/xcms.conf`文件：
```
server {
    listen       80;
    server_name xingweidong.com www.xingweidong.com;

    location / {
        # redirect any requests to the same URL but on https
        return 301 https://$host$request_uri;
    }
}

# HTTPS server
#
server {
    listen       443 ssl;
    server_name xingweidong.com www.xingweidong.com;

    ssl_certificate /etc/letsencrypt/live/www.xingweidong.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.xingweidong.com/privkey.pem;

    # write access and error logs to /var/log
    access_log /var/log/nginx/xcms_access.log;
    error_log /var/log/nginx/xcms_error.log;

    location /server {
        proxy_pass http://127.0.0.1:3031/;
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
```
对于上面的 `proxy_pass http://127.0.0.1:3031/;`，有没有最后的 `/` ，效果对比如下：

配置 | 客户端访问uri | 后台接受到的uri
---|---|---
proxy_pass http://127.0.0.1:3031/; | /server/hello | /hello
proxy_pass http://127.0.0.1:3031; | /server/hello | /server/hello


重载nginx：`systemctl reload nginx`

开始启动后，服务无法正常运行，观察`/var/log/nginx/error.log`发现问题：
```
connect() to 127.0.0.1:3031 failed (13: Permission denied) while connecting to upstream
```
网上查阅资料后，解决方案是执行以下命令：(以后有时间再细究)
```
setsebool -P httpd_can_network_connect 1
```
