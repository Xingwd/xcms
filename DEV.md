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
