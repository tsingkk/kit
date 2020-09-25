import os
import json
import filecmp
import shutil
import time


def getdirname(apath):
    files = os.listdir(apath)
    dirname = [i for i in files if os.path.isdir(os.path.join(apath, i))]
    return dirname


datapath = os.path.join(os.getcwd(), '.kit', 'data.json')
with open(datapath, 'r') as f:
    b = json.load(f)

logpath = os.path.join(os.getcwd(), '.kit', 'log.json')
with open(logpath, 'r') as f:
    logfile = json.load(f)

versforlognum = [int(i) for i in logfile.keys()]
print('\n', '-'*10, '以下版本可供发布', '-'*10, '\n')
for i in logfile:
    print(i)
while True:
    vers = input('输入选择发布的版本号（默认为最新）：')
    if vers == '':
        vers = str(max(versforlognum))
        break
    elif vers in logfile.keys():
        break
    else:
        print('所输入版本号不存在，请重新输入！')

wdpath = os.path.join(os.getcwd(), '1工作')
print('\n', '-'*10, '以下文件包可供发布', '-'*10, '\n')
dirsnames = getdirname(wdpath)
for i in dirsnames:
    print(i)
while True:
    packs = input('输入选择发布的文件包的序号(默认1)：')
    if packs == '':
        packs = 1
        break
    elif int(packs) in range(1, len(dirsnames)+1):
        packs = int(packs)
        break
    else:
        print('所输入文件包的序号不存在，请重新输入！')
lenth = len(dirsnames[packs-1])

versionnum = input('输入发布包名称及版本号（名称-版本号）：')

typeofpack = ['1专业成稿',
              '2提出条件',
              '3过程控制文件',
              '4工艺计算文件',
              '5校核文件'
              ]

versfiles = b['versions'][vers]
reversfiles = [i for i in versfiles if dirsnames[packs-1] in i]
# print(reversfiles)
# print(cwdpath)
for afile in reversfiles:
    afilefrompath = os.path.join(os.getcwd(), '.kit', 'resource', afile)
    afiletopath = os.path.join(os.getcwd(),
                               '2发布',
                               typeofpack[packs-1],
                               versionnum,
                               afile[lenth+1::])
    afiledirname = os.path.dirname(afiletopath)
    # print(afilefrompath)
    # print(afiletopath)
    # print(afiledirname)
    if not os.path.exists(afiledirname):
        os.makedirs(afiledirname)
    shutil.copy2(afilefrompath, afiletopath)

updatepath = os.path.join(os.getcwd(), '.kit', 'update.json')
with open(updatepath, 'r') as f:
    updatemsg = json.load(f)
versforlog = [i for i in logfile.keys() if int(i) <= int(vers)]
for i in updatemsg:
    versforlog = set(versforlog) - set(updatemsg[i]['lognum'])
nowstrTime = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
logs = '# ' + versionnum + '更新说明，' + nowstrTime + '\n'
for i in ('新增', '移除', '修复', '重构', '文档', '格式', '其他'):
    logs += '## ' + i + '\n'
    for j in versforlog:
        for k in logfile[j]['修改记录'][i]:
            logs += '- ' + k + '\n'
logs += '-----\n'
for i in updatemsg:
    logs += updatemsg[i]['update']
updatelogpath = os.path.join(os.getcwd(),
                             '2发布',
                             typeofpack[packs-1],
                             versionnum,
                             '更新说明.md'
                             )
with open(updatelogpath, 'w') as f:
    f.write(logs)
updatemsg[versionnum] = {}
updatemsg[versionnum]['lognum'] = list(versforlog)
updatemsg[versionnum]['update'] = logs
with open(updatepath, 'w') as f:
    json.dump(updatemsg, f, ensure_ascii=False)
print('***', versionnum, '***发布成功！')
