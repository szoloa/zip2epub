# zip转epub
ehentai下载的zip文件转换epub格式电子书方便阅读

    python window.py
    # 依赖tkinter, ebooklib

推荐使用moon reader，通过将间距和页面空白调整为0，翻页动画为无，既有漫画阅读器的效果。 

或者使用命令行

    python main.py ipt1 ipt2 ...
    python main.py --capter ipt1 ip2 ... # 转换带有章节的zip文件
    python main.py --cover coverfile ipt1 ipt ipt3 # 自定义封面 
    # 依赖 ebooklib, toml
清理缓存 

    python main.py --clear

转换为PDF

    python zip2pdf.py ipt1 ipt2 ...
    # 依赖reportlab, pillow, pypdf2

转换后的文件保存在输入的压缩包路径处

## 程序的处理过程
先把压缩包解压到程序所在目录的cache文件夹下，然后读取文件信息，通过python的sort()对图片进行排序，调用ebooklib或者reportlab把图片转换成对应的格式，然后删除cache文件夹
