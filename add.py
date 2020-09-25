import status
import os
import shutil


print('\n', '-'*15, '更新缓存区前', '-'*15, '\n')
difflist = status.getdiff()
bd = os.path.join(
        os.getcwd(),
        '.kit',
        'temp'
    )
wd = os.path.join(
        os.getcwd(),
        '1工作'
    )
for i in difflist['delf']:
    os.remove(os.path.join(bd, i))
for i in difflist['newf']:
    fpath = os.path.join(bd, i)
    dirname = os.path.dirname(fpath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    shutil.copy2(os.path.join(wd, i), fpath)
for i in difflist['modifyf']:
    shutil.copy2(os.path.join(wd, i), os.path.join(bd, i))
print('\n', '-'*15, '更新缓存区后', '-'*15,  '\n')
status.getdiff()
