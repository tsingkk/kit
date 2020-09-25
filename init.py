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
a = {
    'author': author,
    'email': mymail,
    'head': (),
    'versions': {}
}
with open(jsonpath, 'w') as f:
    json.dump(a, f)
# 生成忽略特定扩展名文件
b = {'ign': []}
ignpath = os.path.join(os.getcwd(), '.kit', 'ign.json')
with open(ignpath, 'w') as f:
    json.dump(b, f)
# 生成提交修改记录文件
c = {}
logpath = os.path.join(os.getcwd(), '.kit', 'log.json')
with open(logpath, 'w') as f:
    json.dump(c, f)
# 生成发布文件更新说明记录文件
d = {'太极': {'lognum': [], 'update': ""}}
updatepath = os.path.join(os.getcwd(), '.kit', 'update.json')
with open(updatepath, 'w') as f:
    json.dump(d, f)
# 生成提交修改记录markdown文件
words = '此文件记录版本修改\n-----\n'
mdpath = os.path.join(os.getcwd(), '.kit', 'log.md')
with open(mdpath, 'w') as f:
    f.write(words)
# 生成缓冲区目录temp
temppath = os.path.join(os.getcwd(), '.kit', 'temp')
os.makedirs(temppath)
# 生成版本库目录resource
respath = os.path.join(os.getcwd(), '.kit', 'resource')
os.makedirs(respath)
