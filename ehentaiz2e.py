import zipfile
from z2bookobj import usrEpubBook
import os

def tt(o):
    return int(o.split('_')[0])

def z2b(xname, cover = None, cpname = None, sortby = tt, string = None):
    if cpname == None:
        cpname = 'capter 1'
    dr = f'.cache/{xname[:-4]}/'
    drr = f'.cache/{xname[:-3]}/{cpname}'
    if not os.path.exists(drr):
        os.makedirs(drr)
    # 解压 zip 文件
    with zipfile.ZipFile(f'./.cache/{xname}', 'r') as zip_ref:
        zip_ref.extractall(drr)  # 解压到指定目录
    try:
        t = [(cpname, sorted(os.listdir(drr), key=sortby))]
    except:
        t = [(cpname, sorted(os.listdir(drr)))]
    if cover == None:
        usrEpubBook(t, dr, drr+'/'+t[0][1][0], string)
    else:
        usrEpubBook(t, dr, cover, string)
    
if __name__ == '__main__':
    z2b('[Pixiv] 鬼鳴らす(真理探求者) (1284629) [2024-05-22].zip', 'cover.jpg')