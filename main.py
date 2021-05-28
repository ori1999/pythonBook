import os
'''
批量生成文件夹及文件
'''
# for i in range(1,12):
#     if len(str(i)) == 1:
#         os.mkdir(f'chapter_0{i}')
#     else:
#         os.mkdir(f'chapter_{i}')
a = '6'
os.chdir(f'chapter_0{a}')
for i in range(1,13):
    try:
        with open(f'{a}-{i}.py','w',encoding='utf-8') as f:
            f.close()
    except:
        pass
