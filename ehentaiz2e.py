import zipfile
from z2bookobj import usrEpubBook
import os

def z2b(xname, cover = None, cpname = None):
    if cpname == None:
        cpname = 'capter 1'
    dr = f'.cache/{xname[:-4]}'
    drr = f'.cache/{xname[:-3]}/{cpname}'
    print(f'正在转换{xname[:-4]}')
    if not os.path.exists(drr):
        os.makedirs(drr)
    # 解压 zip 文件
    with zipfile.ZipFile(f'./.cache/{xname}', 'r') as zip_ref:
        zip_ref.extractall(drr)  # 解压到指定目录
    try:
        t = [(cpname, sorted(os.listdir(drr)))]
    except:
        t = [(cpname, sorted(os.listdir(drr)))]
    if cover == None:
        usrEpubBook(t, dr, drr+'/'+t[0][1][0], title=xname[:-4])
    else:
        usrEpubBook(t, dr, cover)
