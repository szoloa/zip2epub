from ebooklib import epub
from ebooklib.plugins import standard
import random

class usrEpubBook(epub.EpubBook):
    '''
    从文件目录创建EPUB漫画。

    ranger_cpter: 章节和图片信息。例如[['第一章', ['/path/to/capter2/1.jpg']], ['第二章',['/path/to/capter2/1.jpg']]] 

    bookname: 创建漫画的名字。

    cover: 封面图片。

    这个的同一章节的图片会放在同一个的页面。

    '''
    def __init__(self, range_cpter, bookname, cover, title=None):
        super().__init__()
        if title == None:
            title = bookname
        self.set_identifier(f'comic{random.randint(0, 500000)}')
        self.set_title(title)
        self.set_language('en')
        self.bookname = bookname
        self.cover = cover
        self.add_author('Danko Bananko', 
                        file_as='Gospodin Danko Bananko', 
                        role='ill', 
                        uid='ctreator')

        self.style = '''img {
    display: block;
    margin: 0;
    padding: 0;
    width: 100%;
    height: auto;
}'''
        default_css = epub.EpubItem(uid="style_default", 
                            file_name="style/default.css", 
                            media_type="text/css", 
                            content=self.style)

        self.add_item(default_css)
        self.setCover()
        self.setContent(range_cpter)
        # print(bookname)
        nav_item = epub.EpubNav()
        self.add_item(nav_item)

        epub.write_epub(f'{bookname}/output.epub', self, {'plugins': [standard.SyntaxPlugin()]})
        
    def setCover(self):
        cover_image = epub.EpubImage()
        cover_image.file_name = 'cover.jpg' 
        cover_image.content = open(self.cover, 'rb').read()
        self.set_cover(cover_image.file_name, cover_image.content)
        self.spine = ['cover']

    def setContent(self, range_capter):
        default_css = epub.EpubItem(uid="style_default", 
                            file_name="../style/default.css", 
                            media_type="text/css", 
                            content=self.style)
        c = []
        toc_items = []
        for j in range_capter:
            c1 = epub.EpubHtml(title=f'{j[0]}', file_name=f'html/capter_{j[0]}.xhtml')
            c1.content = ''
            total_images = len(j[1])
            for idx, i in enumerate(j[1]):
                photo = epub.EpubImage()
                photo.file_name = f'jpg/{j[0]}/{i}'
                photo.media_type = 'image/webp'
                photo.content = open(f'{self.bookname}/{j[0]}/{i}', 'rb').read()
                self.add_item(photo)
                c1.content += '''<p><img src="../jpg/%s/%s" alt="Comic img"'/></p>''' % (j[0], i)
                print(f'\r正在处理: {idx + 1}/{total_images} ({(idx + 1) / total_images:.2%})', end='')
            print(f'\n章节 "{j[0]}" 处理完成！')
            toc_items.append(c1)
            c1.set_language('hr')
            c1.properties.append('rendition:layout-pre-paginated rendition:orientation-landscape')
            c1.add_item(default_css)
            self.add_item(c1)
            c.append(c1)
        self.spine += [*c]
        self.toc = tuple(toc_items)  
        