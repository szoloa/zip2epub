import zipfile 
import shutil
import pathlib
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import os
import sys
import getopt

class usrPdfBook:
    def __init__(self, filename, filelist):
        self.pdf_filename = filename
        self.base_width = letter[0]  # 使用letter宽度，可根据需要更改为其他值
        self.canvasPage = canvas.Canvas(filename)
        self.canvasPage.setTitle(pathlib.Path(filename).stem)
        total_images = len(filelist)
        for idx, i in enumerate(filelist):
            print(f'\r正在处理: {idx + 1}/{total_images} ({(idx + 1) / total_images:.2%})', end='')
            self.addPage(i)
        self.canvasPage.save()        
        print('\n转换完成')
    def addPage(self, image):
        pil_image = Image.open(image)
        image_width, image_height = pil_image.size
        scale_factor = self.base_width / image_width
        new_width = self.base_width
        new_height = image_height * scale_factor
        self.canvasPage.setPageSize((self.base_width, new_height))
        self.canvasPage.drawImage(ImageReader(image), 0, 0, width=new_width, height=new_height)
        self.canvasPage.showPage()

def createPdfWithoutCapter(pathraw):
    (filepath, filename) = os.path.split(pathraw)
    path = pathlib.Path(pathraw)
    if not os.path.exists(f'.cache/{path.stem}'):
        os.makedirs(f'.cache/{path.stem}')
    with zipfile.ZipFile(f'{path}', 'r') as zip_ref:
        zip_ref.extractall(f'.cache/{path.stem}')
    imagelist = [f'.cache/{path.stem}/{i}' for i in sorted(os.listdir(f'.cache/{path.stem}'))]
    usrPdfBook(f'.cache/{path.stem}.pdf', imagelist)
    shutil.copy(f'.cache/{path.stem}.pdf', f'{filepath}/{path.stem}.pdf')    
    shutil.rmtree('.cache')

def main(argv):
    convert = createPdfWithoutCapter
    try:
        opts, args = getopt.getopt(argv, "hc", ['clear','capter','help','cover='])
    except getopt.GetoptError as e:
        print(e)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print ('zip2epub.py  <inputfile1> <inputfil2> ...')
            sys.exit()
        elif opt in ('--clear'):
            clear()
            sys.exit()
        elif opt in ('--cover'):
            cover = arg
        elif opt in ('--capter', '-c'):
            convert = comic
    for arg in args:
        convert(arg)    

if __name__ == '__main__':    
    main(sys.argv[1:])
