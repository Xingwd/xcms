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


安装 Elasticsearch：
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:6.4.2

```
运行 Elasticsearch：
```
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.4.2
```

参考：https://www.elastic.co/guide/en/elasticsearch/reference/6.4/docker.html