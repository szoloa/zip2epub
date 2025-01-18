import zipfile
from z2bookobj import usrEpubBook
import os

def z2b(comicName, pic_cover = None, capterName = None, string = None):
    comic_name, comic_extension = os.path.splitext(comicName)
    comicExtractPath = f'.cache/{comic_name}'
    print(f'正在转换{comic_name}')

    # 解压 zip 文件
    with zipfile.ZipFile(f'./.cache/{comicName}', 'r') as zip_ref:
        zip_ref.extractall(comicExtractPath)  # 解压到指定目录
    try:
        t = [(i, sorted(os.listdir(f'{comicExtractPath}/{i}'))) for i in sorted(os.listdir(comicExtractPath))]
    except Exception as e:
        t = None
        print(e)
    if pic_cover == None:
        usrEpubBook(t, comicExtractPath, comicExtractPath+'/'+t[0][0]+'/'+t[0][1][0], title=comic_name)
    else:
        usrEpubBook(t, comicExtractPath, pic_cover, title=comic_name)
