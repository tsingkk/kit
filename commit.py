import status
import os
import shutil
import time
import json


def multiline(tishi):
    words = []
    while True:
        aline = input(tishi)
        if aline == 'wq':
            break
        words.append(aline)
    return words


# 生成提交时间戳
nowstrTime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

# 生成修改记录并保存至 log.json
logpath = os.path.join(os.getcwd(), '.kit', 'log.json')
with open(logpath, 'r') as f:
    b = json.load(f)
b[nowstrTime] = {}
b[nowstrTime]['修改记录'] = {}
for i in ('新增', '移除', '修复', '重构', '文档', '格式', '其他'):
    b[nowstrTime]['修改记录'][i] = multiline('修改记录-->' + i + '：')
b[nowstrTime]['修改依据'] = multiline('修改依据：')
b[nowstrTime]['影响范围'] = multiline('影响范围：')
b[nowstrTime]['修改目的'] = multiline('修改目的：')
with open(logpath, 'w') as f:
    json.dump(b, f, ensure_ascii=False)

# 将修改记录输出为markdown文件，方便浏览
alog = '# ' + nowstrTime + '\n'
for key1 in b[nowstrTime]:
    alog += '## ' + key1 + '\n'
    if key1 == '修改记录':
        for key2 in b[nowstrTime][key1]:
            alog += '### ' + key2 + '\n\n'
            for i in b[nowstrTime]['修改记录'][key2]:
                alog += '- ' + i + '\n'
            alog += '\n'
    else:
        for i in b[nowstrTime][key1]:
            alog += '- ' + i + '\n'
        alog += '\n'
alog += '-----\n'
mdpath = os.path.join(os.getcwd(), '.kit', 'log.md')
with open(mdpath, 'a') as f:
    f.write(alog)

# 将缓存区文件拷贝至版本库，生成并记录每个版本的文件索引
jsonpath = os.path.join(os.getcwd(), '.kit', 'data.json')
with open(jsonpath, 'r') as f:
    a = json.load(f)

bd = os.path.join(
        os.getcwd(),
        '.kit',
        'temp'
    )
bdfiles = status.getallfiles(bd)
newbdfiles = []
for i in bdfiles:
    pathi = os.path.join(bd, i)
    mtimef = os.path.getmtime(pathi)
    localTime = time.localtime(mtimef)
    strTime = time.strftime('%Y%m%d%H%M%S', localTime)
    newname = os.path.splitext(i)[0] + '-' + strTime + \
        os.path.splitext(i)[1]
    newbdfiles.append(newname)
    dstdir = os.path.join(os.getcwd(), '.kit', 'resource')
    if newname not in a['head']:
        dirname = os.path.join(dstdir, os.path.dirname(i))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        shutil.copy2(pathi, os.path.join(dstdir, newname))

a["versions"][nowstrTime] = newbdfiles
a['head'] = newbdfiles
with open(jsonpath, 'w') as f:
    json.dump(a, f, ensure_ascii=False)
