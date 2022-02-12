from funcs import *
from Find_stu_notupload import *
'''
使用方法，再raw目录中仅放一对腾讯收集表导出的文件，即批量导出的zip和xlsx文件。
所以用一次就要清除一次，保证每次用前raw下是空的。
'''


zip_pth, exl_pth = get_rawfiles_pth() # 获取腾讯收集表两个导出文件的地址

nicknames, targetnames = get_target_names(exl_pth) # 获取昵称和提交者真实姓名，昵称用于对后续附近对号入座重命名

raw_names_list = get_raw_names(zip_pth)# 原始的解压zip中文件的名称，带昵称和日期很凌乱


## 重命名开始
print("已经重新命名：\n")
for rawfile_name in raw_names_list:
    typename = get_type_name(rawfile_name)# 获取文件格式
    for nickname in nicknames:
        if str(nickname) in rawfile_name:#如果昵称对位了即更改其名称,使用str（）防止出现诡异的昵称
            targetname = targetnames[nicknames.index(nickname)] + typename# 获取对位的目标名称
            print('{:-^25}'.format(targetname))
            #更改目标文件名称
            src = os.path.join(accessory_pth, rawfile_name)
            dst = os.path.join(accessory_pth, targetname)
            os.rename(src, dst)
            break
print('#{:=^30}#'.format('结束'))

# print('没有交：{}'.format(get_stunames_notupload(tx1902_nameslist_exlPth, target_pth)))



