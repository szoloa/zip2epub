import sys
import shutil
import os
import ehentaiz2e

if not os.path.exists('./.cache'):
    os.makedirs('./.cache')

if sys.argv[1] == 'clear':
    shutil.rmtree('./.cache')
    print('缓存清理完成')
    exit()

for i in sys.argv[1:]:
    (filepath, filename) = os.path.split(i)
    try:
        shutil.copy(i, f'./.cache/{filename}')
    except FileExistsError:
        pass
    except Exception as e:
        print(e)
    ehentaiz2e.z2b(filename)
    try:
        shutil.copy(f'./.cache/{filename[:-4]}/output.epub', f'{filepath}/{filename[:-4]}.epub')
    except FileExistsError:
        pass
    except Exception as e:
        print(e)
shutil.rmtree('./.cache')
print('转换完成')