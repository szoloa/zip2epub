import sys
import shutil
import os
import ehentaiz2e
import comicz2e
import getopt

cover = None

if not os.path.exists('./.cache'):
    os.makedirs('./.cache')

def clear():
    shutil.rmtree('./.cache')
    print('缓存清理完成')

def ehentai(args):
    for i in args:
        (filepath, filename) = os.path.split(i)
        try:
            shutil.copy(i, f'./.cache/{filename}')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
        ehentaiz2e.z2b(filename, cover=cover)
        try:
            shutil.copy(f'./.cache/{filename[:-4]}/output.epub', f'{filepath}/{filename[:-4]}.epub')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
    shutil.rmtree('./.cache')
    print('转换完成')

def comic(args):
    for i in args:
        (filepath, filename) = os.path.split(i)
        try:
            shutil.copy(i, f'./.cache/{filename}')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
        comicz2e.z2b(filename, cover=cover)
        try:
            shutil.copy(f'./.cache/{filename[:-4]}/output.epub', f'{filepath}/{filename[:-4]}.epub')
        except FileExistsError:
            pass
        except Exception as e:
            print(e)
    shutil.rmtree('./.cache')
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