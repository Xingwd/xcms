# xcms
我的内容管理系统，个人网站


启动：
```
export FLASK_APP=xcms.py
export FLASK_ENV=development
flask run
```


数据库迁移操作：
```
flask db init
flask db migrate
flask db upgrade
```