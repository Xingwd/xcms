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