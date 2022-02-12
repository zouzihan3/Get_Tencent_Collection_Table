import os
import pandas as pd
'''
寻找对应目录下文件名，以判断谁没有交
'''
# 名单目录
tx1902_nameslist_exlPth = 'C:\\User\\Dev\\Projects\\python\\tool\\rename_tencent_Collection\\data\\otherSource\\样例名单.xlsx'# 班级名单目录
# 要被检测的目录
target_pth = 'C:\\User\\Dev\\Projects\\python\\tool\\rename_tencent_Collection\\data\\raw\\decompression_files'

def get_stunames_notupload(exl_pth, target_pth):# 获取谁没交
    exl_data = pd.read_excel(exl_pth) # 导入excel
    all_stu_names = list(exl_data['姓名'])# 读取所有同学姓名列表
    temp_stu_names = all_stu_names
    filenames = os.listdir(target_pth)
    for filename in filenames:# 遍历寻找未交同学
        for stuname in all_stu_names:
            if stuname in filename:
                temp_stu_names.remove(stuname)
                break
        continue

    return temp_stu_names



