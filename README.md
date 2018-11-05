# xcms
我的内容管理系统，个人网站


pip国内源：-i https://pypi.tuna.tsinghua.edu.cn/simple


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

自定义命令：
```
flask createadmin --help
flask createadmin --name admin --password admin
```