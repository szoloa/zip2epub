from ebooklib import epub
from ebooklib.plugins import standard
import os
import random

# range_cpter 列表 元素为元组 元组第一个元素为章节名

class usrEpubBook(epub.EpubBook):
    def __init__(self, range_cpter, bookname, cover):
        super().__init__()
        self.set_identifier(f'comic{random.randint(0, 500000)}')
        self.set_title(bookname)
        self.set_language('en')
        self.bookname = bookname
        self.cover = cover
        self.add_author('Aleksandar Erkalovic')
        self.add_author('Danko Bananko', 
                        file_as='Gospodin Danko Bananko', 
                        role='ill', 
                        uid='coauthor')

        self.style = '''img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
                        '''
        default_css = epub.EpubItem(uid="style_default", 
                            file_name="style/default.css", 
                            media_type="text/css", 
                            content=self.style)

        self.add_item(default_css)
        self.setCover()
        self.setContent(range_cpter)
        print(bookname)
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
            for i in j[1]:
                photo = epub.EpubImage()
                photo.file_name = f'jpg/{j[0]}/{i}'
                photo.media_type = 'image/jpeg'
                photo.content = open(f'{self.bookname}/{j[0]}/{i}', 'rb').read()
                self.add_item(photo)
                c1.content += '''<p><img src="../jpg/%s/%s" alt="Comic img"'/></p>''' % (j[0], i)
                print(f'\r{i}/{len(j[1])}', end='')
            c1.set_language('hr')
            c1.properties.append('rendition:layout-pre-paginated rendition:orientation-landscape')
            c1.add_item(default_css)
            self.add_item(c1)
            c.append(c1)
        self.spine += [*c]

if __name__ == '__main__':
    t = []
    def t(o):
        return int(o.split('-')[-1].split('.')[0])
    t = [('np', sorted(os.listdir('[Eromazun_(Ma-kurou)]_Mesu_Ochi_Onna_Muzan-sama_-_RAPE_OF_DEMON_SLAYER_4_(Kimetsu_no_Yaiba)_[Chinese]_[瑞树汉化组]_[Digital]/np'), key=t))]
    usrEpubBook(t, '[Eromazun_(Ma-kurou)]_Mesu_Ochi_Onna_Muzan-sama_-_RAPE_OF_DEMON_SLAYER_4_(Kimetsu_no_Yaiba)_[Chinese]_[瑞树汉化组]_[Digital]', 'cover.jpg')
        