# 环境依赖文件
## 导出环境依赖
```bash
pip freeze > requirements.txt
```
## 恢复环境
```bash
pip install -r requirements.txt
```

# 生成秘钥
生成一个好的`SECRET_KEY`的方法：
```bash
python -c 'import os; print(os.urandom(24))'
```
工程配置中已经做了安全措施，如果没有配置这个秘钥，将通过这种方式自动生成一个。


# 开发调试
## flask
### 使用flask命令
```
source activate xcms
export FLASK_APP=xcms.py
export FLASK_ENV=development
flask run
```
### 直接启动
```
source activate xcms
python xcms.py
```


# 测试
## Python
### Flask
使用`pytest`测试工具，测试代码都写在`server/tests`目录下

#### 执行测试
在server目录下，直接执行命令：`pytest`。

#### 衡量测试覆盖率
使用`coverage`命令代替直接使用`pytest`来运行测试：`coverage run -m pytest`

查看覆盖率报告：`coverage report`

生成HTML报告：`coverage html`
