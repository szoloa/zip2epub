from ebooklib import epub
from ebooklib.plugins import standard
import random

class usrEpubBook(epub.EpubBook):
    def __init__(self, range_cpter, bookname ,cover, string, title=None):
        super().__init__()
        if title == None:
            title = bookname
        self.set_identifier(f'comic{random.randint(0, 500000)}')
        self.set_title(title)
        self.set_language('en')
        self.bookname = bookname
        self.cover = cover
        self.string = string
        self.add_author('Aleksandar Erkalovic')
        self.add_author('Danko Bananko', 
                        file_as='Gospodin Danko Bananko', 
                        role='ill', 
                        uid='coauthor')

        self.style = '''
img {
    display: block;
    margin: 0;
    padding: 0;
    width: 100%;
    height: auto;
}
'''
        default_css = epub.EpubItem(uid="style_default", 
                            file_name="style/default.css", 
                            media_type="text/css", 
                            content=self.style)

        self.add_item(default_css)
        self.setCover()
        self.setContent(range_cpter)
        # print(bookname)
        epub.write_epub(f'{bookname}output.epub', self, {'plugins': [standard.SyntaxPlugin()]})
        
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
        for j in range_capter:
            c1 = epub.EpubHtml(title=f'{j[0]}', file_name=f'html/chpter_{j[0]}.xhtml')
            c1.content = ''
            total_images = len(j[1])
            for idx, i in enumerate(j[1]):
                photo = epub.EpubImage()
                photo.file_name = f'jpg/{j[0]}/{i}'
                photo.media_type = 'image/jpeg'
                photo.content = open(f'{self.bookname}/{j[0]}/{i}', 'rb').read()
                self.add_item(photo)
                c1.content += '''<p><img src="../jpg/%s/%s" alt="Comic img"'/></p>''' % (j[0], i)
                print(f'\r正在处理: {idx + 1}/{total_images} ({(idx + 1) / total_images:.2%})', end='')
            print()
            c1.set_language('hr')
            c1.properties.append('rendition:layout-pre-paginated rendition:orientation-landscape')
            c1.add_item(default_css)
            self.add_item(c1)
            c.append(c1)
        self.spine += [*c]
        