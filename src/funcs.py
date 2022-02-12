import zipfile
import pandas as pd
import os
'''
使用方法，再raw目录中仅放一对腾讯收集表导出的文件，即批量导出的zip和xlsx文件。
所以用一次就要清除一次，保证每次用前raw下是空的。
'''

raw_pth = os.path.abspath(
    os.path.dirname(os.getcwd()) + os.path.sep + "./data/raw/")  # 从腾讯文档批量导出的附件地址

accessory_pth = os.path.join(raw_pth, 'decompression_files') # zip解压出的附件目录

def del_history_files():#删除上次解压出的全部zip文件附件，防止与本次使用串扰
    del_list = os.listdir(accessory_pth)
    for f in del_list:
        file_path = os.path.join(accessory_pth, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

def get_rawfiles_pth():#获取zip和xlsx文件地址，所以raw文件夹中只能有一对文件出现，即批量导出的zip和xlsx文件。
    for pth in os.listdir(raw_pth):#读取目录下文件名列表，获取对应文件路径
        if'zip' in pth :
            zip_pth = os.path.join(raw_pth, pth)
        if 'xlsx' in pth:
            exl_pth = os.path.join(raw_pth, pth)
    return zip_pth, exl_pth

def get_target_names(exl_pth, name_mod = 'name'):#获取需要更改成的目标名称,需要目标xlsx地址，以及命名模式
    exl_data = pd.read_excel(exl_pth)

    if name_mod == 'name':# 仅姓名模式
        targetnames_list = list(exl_data['学生姓名（必填）'])
        nicknames_list = list(exl_data['提交者（自动）'])

        return nicknames_list, targetnames_list


def get_raw_names(zip_pth):#获取原始名称，往往为qq名称，此处先解压后获取.
    del_history_files() # 删除上次附件防止与本次串扰
    with zipfile.ZipFile(zip_pth,'r') as zip:
        zip.extractall(accessory_pth)
    raw_names_list = os.listdir(accessory_pth)
    return raw_names_list

def get_type_name(filename):# 获取文件格式
    temp_str = filename[-5::] # 取文件全名后五个字符
    index_point = temp_str.index('.')
    typername = temp_str[index_point::] # 根据 . 的位置片选出类型
    return typername

