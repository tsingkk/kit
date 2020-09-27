import os
import json

# 生成作者信息
author = input('输入作者名称：')
mymail = input('输入作者邮箱：')
# 如果.kit目录不存在则创建
kitpath = os.path.join(os.getcwd(), '.kit')
if not os.path.exists(kitpath):
    os.makedirs(kitpath)
# 生成版本记录文件
jsonpath = os.path.join(os.getcwd(), '.kit', 'data.json')
if os.path.exists(jsonpath):
    print('data.json已存在，使用原有data.json文件！')
else:
    a = {
         'author': author,
         'email': mymail,
         'head': (),
         'versions': {}
         }
    with open(jsonpath, 'w') as f:
        json.dump(a, f)
    print('data.json文件创建成功！')
# 生成忽略特定扩展名文件
ignpath = os.path.join(os.getcwd(), '.kit', 'ign.json')
if os.path.exists(ignpath):
    print('ign.json已存在，使用原有ign.json文件！')
else:
    b = {'ign': []}
    with open(ignpath, 'w') as f:
        json.dump(b, f)
    print('ign.json文件创建成功！')
# 生成提交修改记录文件
logpath = os.path.join(os.getcwd(), '.kit', 'log.json')
if os.path.exists(logpath):
    print('log.json已存在，使用原有log.json文件！')
else:
    c = {}
    with open(logpath, 'w') as f:
        json.dump(c, f)
    print('log.json文件创建成功！')
# 生成提交修改记录markdown文件
mdpath = os.path.join(os.getcwd(), '.kit', 'log.md')
if os.path.exists(mdpath):
    print('log.md已存在，使用原有log.md文件！')
else:
    words = '此文件记录版本修改\n-----\n'
    with open(mdpath, 'w') as f:
        f.write(words)
    print('log.md文件创建成功！')
# 生成发布文件更新说明记录文件
updatepath = os.path.join(os.getcwd(), '.kit', 'update.json')
if os.path.exists(updatepath):
    print('update.json已存在，使用原有update.json文件！')
else:
    d = {'太极': {'lognum': [], 'update': ""}}
    with open(updatepath, 'w') as f:
        json.dump(d, f)
    print('update.json文件创建成功！')
# 生成缓冲区目录temp
temppath = os.path.join(os.getcwd(), '.kit', 'temp')
if os.path.exists(temppath):
    print('temp目录已存在，使用原有temp目录！')
else:
    os.makedirs(temppath)
    print('temp目录创建成功！')
# 生成版本库目录resource
respath = os.path.join(os.getcwd(), '.kit', 'resource')
if os.path.exists(respath):
    print('resource目录已存在，使用原有resource目录！')
else:
    os.makedirs(respath)
    print('resource目录创建成功！')
