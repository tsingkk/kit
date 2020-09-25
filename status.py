# 显示工作目录与缓存区差别

import os
import json
import filecmp


def getallfiles(path):
    ignpath = os.path.join(
        os.getcwd(),
        '.kit',
        'ign.json'
    )
    with open(ignpath, 'r') as f:
        a = json.load(f)
        ignlist = a['ign']
    flist = []
    for root, dirs, fs in os.walk(path):
        for f in fs:
            if os.path.splitext(f)[-1][1:] not in ignlist:
                f_fullpath = os.path.join(root, f)
                f_relativepath = f_fullpath[(len(path)+1):]
                flist.append(f_relativepath)
    return flist


# configpath = os.path.join(
#     os.getcwd(),
#     '.kit',
#     'kitconfig.json'
# )
# with open(configpath, 'r') as f:
#     a = json.load(f)
#     data = a['cwbranch']

def getdiff():
    a = {}
    bd = os.path.join(
        os.getcwd(),
        '.kit',
        'temp'
    )
    print('缓存区：', bd)
    wd = os.path.join(
        os.getcwd(),
        '1工作'
    )
    print('工作区：', wd)
    wdfiles = set(getallfiles(wd))
    bdfiles = set(getallfiles(bd))
    a['newf'] = wdfiles - bdfiles
    a['delf'] = bdfiles - wdfiles
    commonfiles = list(wdfiles & bdfiles)
    # print('同名文件：', commonfiles)
    match, mismatch, errors = filecmp.cmpfiles(wd,
                                               bd,
                                               commonfiles,
                                               shallow=False)
    # print('匹配：', match)
    # print('不匹配：', mismatch)
    # print('错误：', errors)
    a['modifyf'] = mismatch
    print('\n', '-'*10, '以下文件被修改', '-'*10, '\n')
    for f in a['modifyf']:
        print(f)
    print('\n', '-'*10, '以下文件未加入缓存区', '-'*10, '\n')
    for f in a['newf']:
        print(f)
    print('\n', '-'*10, '以下文件将从缓存区中删除', '-'*10, '\n')
    for f in a['delf']:
        print(f)
    return a
    filecmp.clear_cache()


if __name__ == "__main__":
    getdiff()
