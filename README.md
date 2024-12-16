# zip转epub
ehentai下载的zip文件转换epub格式电子书方便阅读

    python window.py

依赖 

    tkinter
    ebooklib 

推荐使用moon reader，通过将间距和页面空白调整为0，翻页动画为无，既有漫画阅读器的效果。 

或者使用命令行

    python main.py ipt1 ipt2 ...
    python main.py --capter ipt1 ip2 ... # 转换带有章节的zip文件
    python main.py --cover coverfile ipt1 ipt ipt3 # 自定义封面 

清理缓存 

    python main.py clear

