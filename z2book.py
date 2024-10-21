from ebooklib import epub
from ebooklib.plugins import standard
import os
import random


class usrEpubBook():

    def __init__():
        book = epub.EpubBook()

        # add basic metadata
        book.set_identifier(f'comic{random.randint(0, 500000)}')
        book.set_title('Sample book')
        book.set_language('en')

        book.add_author('Aleksandar Erkalovic')
        book.add_author('Danko Bananko', 
                        file_as='Gospodin Danko Bananko', 
                        role='ill', 
                        uid='coauthor')

        # define style for content
        style = '''BODY { text-align: justify;}'''
        default_css = epub.EpubItem(uid="style_default", 
                                    file_name="style/default.css", 
                                    media_type="text/css", 
                                    content=style)

        cover_image = epub.EpubImage()
        cover_image.file_name = 'a.jpg'  # Make sure this file exists in your project directory
        with open('a.jpg', 'rb') as f:
            cover_image.content = f.read()

        book.add_item(cover_image)

        # set cover
        book.set_cover(cover_image.file_name, open('a.jpg', 'rb').read())

        # intro chapter


        cover_image = epub.EpubImage()
        cover_image.file_name = 'cover.jpg'  # 确保图片文件存在于此路径
        with open('cover.jpg', 'rb') as f:
            cover_image.content = f.read()
        book.add_item(cover_image)

        def get_spine():
            # 创建包含封面图片的 HTML 内容
            cover_html = f"""
            <html>
            <head></head>
            <body>
                <div id="cover-image">
                    <img src="cover.jpg" alt="Cover Image" />
                </div>
            </body>
            </html>
            """

            # 创建一个 EpubHtml 对象用于封面
            cover_page = epub.EpubHtml(uid='cover_page', file_name='cover.xhtml', content=cover_html)
            book.add_item(cover_page)

            # 更新 spine，将封面图片页面放在第一位
            book.spine = [cover_page] + book.spine

            return 

        book.spine = [cover_page] + book.spine

        for j in range(len(os.listdir('超天醬臨！'))):
            c1 = epub.EpubHtml(title=f'Chapter {j}', 
                            file_name=f'chpter{j}.xhtml')

            for i in range(len(os.listdir(f'超天醬臨！/第{j+1:02}話'))):
                i = str(i) + '.jpg'
                photo = epub.EpubImage()
                photo.file_name = f'{i}'
                photo.media_type = 'image/jpeg'
                photo.content = open(f'超天醬臨！第01話/{i}', 'rb').read()

                # 将照片添加到 ePub 书中
                book.add_item(photo)

                # 修改 c1.content 来引用照片
                c1.content = str(c1.content) + f'<img src="{i}" alt="Introduction Photo" />'
            
                # set language just for this chapter
                c1.set_language('hr')

                # set properties for this file
                c1.properties.append('rendition:layout-pre-paginated rendition:orientation-landscape')

                # this chapter should also include this css file
                c1.add_item(default_css)

                book.add_item(c1)

        # create table of contents
        # book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
        #             (epub.Section('Languages'),
        #               (c1, ))
        #             )

        # style for navigation file
        style = 'BODY { color: black; }'
        nav_css = epub.EpubItem(uid="style_nav", 
                                file_name="style/nav.css", 
                                media_type="text/css", 
                                content=style)

        # add navigation files
        book.add_item(epub.EpubNcx())

        nav = epub.EpubNav()
        nav.add_item(nav_css)
        book.add_item(nav)

        # add css files
        book.add_item(default_css)
        book.add_item(nav_css)

        # create spine
        book.spine = ['nav', c1]


        # create epub file
        epub.write_epub('test.epub', book, {'plugins': [standard.SyntaxPlugin()]})