import zipfile
from z2bookobj import usrEpubBook
import os

def tt(o):
    return int(o.split('_')[0])

def z2b(xname, cover, cpname = None, sortby = tt):
    
    if cpname == None:
        cpname = 'capter 1'

    dr = f'.cache/{xname}'

    drr = f'.cache/{xname}/{cpname}'

    if not os.path.exists(drr):
        os.makedirs(drr)

    # 解压 zip 文件
    with zipfile.ZipFile(f'{xname}', 'r') as zip_ref:
        zip_ref.extractall(drr)  # 解压到指定目录

    t = [(cpname, sorted(os.listdir(drr), key=sortby))]
    usrEpubBook(t, dr, cover)

if __name__ == '__main__':
    z2b('[Pixiv] 鬼鳴らす(真理探求者) (1284629) [2024-05-22].zip', 'cover.jpg')