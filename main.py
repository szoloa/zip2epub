import sys
import shutil
import os
from .lib import ehentaiz2e
from .lib import comicz2e
import getopt
import toml

try: 
    cacheFolder = toml.load('~/.config/zip2epub/config.toml')[cacheFolder]
except:
    cacheFolder = '~/.cache/zip2epub'

cover = None

if not os.path.exists(cacheFolder):
    os.makedirs(cacheFolder)

def clear():
    if input(f'确认删除{cacheFolder}的所以内容？') == 'y':
        shutil.rmtree(cacheFolder)
        print('缓存清理完成')

def ehentai(args):
    for i in args:
        (filepath, filename) = os.path.split(i)
        comic_name, comic_extension = os.path.splitext(comicName)
        try:
            shutil.copy(i, f'{cacheFolder}/{filename}')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
        ehentaiz2e.z2b(filename, cover=cover)
        if filepath == '':
            filepath = '.'
        try:
            shutil.copy(f'{cacheFolder}/{comic_name}/output.epub', f'{filepath}/{comic_name}.epub')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
            return
    print('转换完成')

def comic(args):
    for i in args:
        (filepath, filename) = os.path.split(i)
        comic_name, comic_extension = os.path.splitext(comicName)
        try:
            shutil.copy(i, f'{cacheFolder}/{filename}')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
        comicz2e.z2b(filename, pic_cover=cover)
        try:
            if not filepath:
                filepath = '.'
            shutil.copy(f'{cacheFolder}/{comic_name}/output.epub', f'{filepath}/{comic_name}.epub')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
            return
    print('转换完成')

def main(argv):
    convert = ehentai
    try:
        opts, args = getopt.getopt(argv, "hc", ['clear','capter','help','cover='])
    except getopt.GetoptError as e:
        print(e)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print ('test.py -i <inputfile>')
            sys.exit()
        elif opt in ('--clear'):
            clear()
            sys.exit()
        elif opt in ('--cover'):
            cover = arg
        elif opt in ('--capter', '-c'):
            convert = comic
    convert(args)

if __name__ == "__main__":
   main(sys.argv[1:])