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
from PyPDF2 import PdfWriter, PdfReader

global cover
cover = None

def clear():
	shutil.rmtree('./.cache')
	print('缓存清理完成')

class usrPdfBook:
    def __init__(self, filename, filelist):
        global cover
        self.pdf_filename = filename
        self.base_width = letter[0] 
        self.canvasPage = canvas.Canvas(filename)
        self.canvasPage.setTitle(pathlib.Path(filename).stem)
        if cover != None:
            self.addPage(cover)
        total_images = len(filelist)
        for idx, i in enumerate(filelist):
            print(f'\r正在处理: {idx + 1}/{total_images} ({(idx + 1) / total_images:.2%})', end='')
            try:
                self.addPage(i)
            except:
                print("失败", idx+1)
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

class usrPdfBookWithCapter(usrPdfBook):
    def __init__(self, filename, filelist):
        global cover
        print('创建pdf',end='')
        self.pdf_filename = filename
        self.base_width = letter[0]  
        self.canvasPage = canvas.Canvas(filename)
        self.canvasPage.setTitle(pathlib.Path(filename).stem)
        page = 0
        if cover != None:
            page +=1
            self.addPage(cover)
        self.bookmarks = []
        total_images = len(filelist)
        for j in filelist:
            total_images = len(j[1])
            print(f'\n{pathlib.Path(j[0]).stem} 处理中')
            self.bookmarks.append({'title' : pathlib.Path(j[0]).stem, 'page_number' : page, 'parent': None})
            for idx, i in enumerate(j[1]):
                print(f'\r正在处理: {idx + 1}/{total_images} ({(idx + 1) / total_images:.2%})', end='')
                self.addPage(f'{j[0]}/{i}')
                page += 1
        self.canvasPage.save()
        self.add_bookmarks(filename)
        print('\n转换完成')

    # 添加目录信息
    def add_bookmarks(self, filename):
        output = PdfWriter()
        pdffile = open(filename, "rb")
        input_pdf = PdfReader(pdffile)
        for bookmark in self.bookmarks:
            output.add_outline_item(
                title=bookmark['title'],
                page_number=bookmark['page_number'],
                parent=bookmark['parent']
            )
        # 复制PDF页面到输出PDF
        for page in range(len(input_pdf.pages)):
            output.add_page(input_pdf.pages[page])
        with open(filename, "wb") as f:
            output.write(f)
        pdffile.close()


def createPdfWithoutCapter(pathraw):
    (filepath, filename) = os.path.split(pathraw)
    path = pathlib.Path(pathraw)
    if not os.path.exists(f'.cache/{path.stem}'):
        os.makedirs(f'.cache/{path.stem}')
    with zipfile.ZipFile(f'{path}', 'r') as zip_ref:
        zip_ref.extractall(f'.cache/{path.stem}')
    imagelist = [f'.cache/{path.stem}/{i}' for i in sorted(os.listdir(f'.cache/{path.stem}'))]
    usrPdfBook(f'.cache/{path.stem}.pdf', imagelist)
    if filepath == '':
        filepath = '.'
    shutil.copy(f'.cache/{path.stem}.pdf', f'{filepath}/{path.stem}.pdf')   
    clear() 

def creatPdfWithCapter(pathraw):
    (filepath, filename) = os.path.split(pathraw)
    path = pathlib.Path(pathraw)
    if not os.path.exists(f'.cache/{path.stem}'):
        os.makedirs(f'.cache/{path.stem}')
    with zipfile.ZipFile(f'{path}', 'r') as zip_ref:
        zip_ref.extractall(f'.cache/{path.stem}')
    capterlist = [(f'.cache/{path.stem}/{i}', sorted(os.listdir(f'.cache/{path.stem}/{i}'))) for i in sorted(os.listdir(f'.cache/{path.stem}'))]
    usrPdfBookWithCapter(f'.cache/{path.stem}.pdf', capterlist)
    if filepath == '':
        filepath = '.'
    shutil.copy(f'.cache/{path.stem}.pdf', f'{filepath}/{path.stem}.pdf')   
    clear()

def main(argv):
    global cover
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
            convert = creatPdfWithCapter
    for arg in args:
        convert(arg)

if __name__ == '__main__':    
    main(sys.argv[1:])
