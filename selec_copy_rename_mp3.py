import os, shutil


work_dir = 'mp3files'


def is_all_zh(s):
    for c in s:
        if not (('\u4e00' <= c <= '\u9fa5') or c in [' ', '，', ':']):
            return False
    if '樊登读书会' in s:
        return False
    return True

def renaming(span):
    str_list = []
    for x in span:
        str_list.append(x)
    rmdic = []
    for x in str_list:
        if x.isdecimal():
            rmdic.append(x)
        elif x in ['《', '》', '.', ' ', '-', '_'] :
            rmdic.append(x)
        elif x in '樊登速读书会' and '樊登' in span:
            rmdic.append(x)
        elif x in '音频':
            rmdic.append(x)
    #print(span)
    #print(rmdic)    
    for x in rmdic:
        str_list.remove(x)

    new_name  = ''
    for x in str_list:
        new_name += x
    
    return new_name


for fildersname, _, filesname in os.walk(work_dir):
    for file in filesname:
        #print(fildersname, file)
        file0 = file.rstrip('.mp3')
        #print(file0)
        if is_all_zh(file0):
            continue
        new_file_name  = renaming(file0) + '.mp3'
        new_file_address = os.path.join(fildersname, new_file_name)
        old_file_name = os.path.join(fildersname, file)
        #print(new_file_name)
        #print(old_file_name)
        print(new_file_address)
        print()
        shutil.move(old_file_name, new_file_address)
        