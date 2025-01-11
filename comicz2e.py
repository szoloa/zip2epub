import zipfile
from zip2epubobj import usrEpubBook
import os

def z2b(xname, cover = None, cpname = None, string = None):
    dr = f'.cache/{xname[:-4]}'
    print(f'正在转换{xname[:-4]}')

    # 解压 zip 文件
    with zipfile.ZipFile(f'./.cache/{xname}', 'r') as zip_ref:
        zip_ref.extractall(dr)  # 解压到指定目录
    try:
        t = [(i, sorted(os.listdir(f'{dr}/{i}'))) for i in sorted(os.listdir(dr))]
    except Exception as e:
        t = None
        print(e)
    if cover == None:
        usrEpubBook(t, dr, dr+'/'+t[0][0]+'/'+t[0][1][0], title=xname[:-4])
    else:
        usrEpubBook(t, dr, cover, title=xname[:-4])
