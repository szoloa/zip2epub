from bs4 import BeautifulSoup as soup
import time
from spider_zip import getImg

host_c = 'https://www.mangacopy.com'

str_c = '<ul><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/d4017cb8-8d7f-11eb-8859-00163e0ca5bd" target="_blank" title="第01话" style="display: block;"><li>第01话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/4213b728-9200-11eb-9095-00163e0ca5bd" target="_blank" title="第02话" style="display: block;"><li>第02话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/d6697a18-9bae-11eb-bfd7-00163e0ca5bd" target="_blank" title="第03话" style="display: block;"><li>第03话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/83773d2a-9e08-11eb-b915-00163e0ca5bd" target="_blank" title="第04话" style="display: block;"><li>第04话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/0b3499b2-a5cd-11eb-bf5c-00163e0ca5bd" target="_blank" title="第05话" style="display: block;"><li>第05话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/c009187a-be3e-11eb-9418-00163e0ca5bd" target="_blank" title="第06话" style="display: block;"><li>第06话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/3a239c14-ca0d-11eb-a203-00163e0ca5bd" target="_blank" title="第07话" style="display: block;"><li>第07话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/4c38c302-d37c-11eb-a122-00163e0ca5bd" target="_blank" title="第08话" style="display: block;"><li>第08话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/2f5bac20-e60c-11eb-9888-00163e0ca5bd" target="_blank" title="第09话" style="display: block;"><li>第09话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/0a042098-f1f5-11eb-ab0e-00163e0ca5bd" target="_blank" title="第10话" style="display: block;"><li>第10话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/0a044bfe-f1f5-11eb-ab0e-00163e0ca5bd" target="_blank" title="第11话" style="display: block;"><li>第11话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/bc9473ce-0a65-11ec-9025-00163e0ca5bd" target="_blank" title="第12话" style="display: block;"><li>第12话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/36f591ca-0e4e-11ec-8749-00163e0ca5bd" target="_blank" title="第13话" style="display: block;"><li>第13话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/078cec30-24fb-11ec-b35c-00163e0ca5bd" target="_blank" title="第14话" style="display: block;"><li>第14话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/1d5eb0f6-4315-11ec-ab8a-00163e0ca5bd" target="_blank" title="第15话" style="display: block;"><li>第15话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/e5865670-53ea-11ec-a544-024352452ce0" target="_blank" title="第16话" style="display: block;"><li>第16话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/18010844-6583-11ec-befc-024352452ce0" target="_blank" title="第17话" style="display: block;"><li>第17话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/243060ba-8d60-11ec-b1fc-024352452ce0" target="_blank" title="第18话" style="display: block;"><li>第18话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/5182f414-a3a0-11ec-9acd-024352452ce0" target="_blank" title="第19话" style="display: block;"><li>第19话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/cd409882-b759-11ec-92ed-024352452ce0" target="_blank" title="第20话" style="display: block;"><li>第20话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/23a60bee-b9a8-11ec-9685-024352452ce0" target="_blank" title="第21话" style="display: block;"><li>第21话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/452a8d4a-c4a1-11ec-81e9-024352452ce0" target="_blank" title="第22话" style="display: block;"><li>第22话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/bec15c8c-e02c-11ec-a4f2-024352452ce0" target="_blank" title="第23话" style="display: block;"><li>第23话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/56468678-eb03-11ec-ae79-024352452ce0" target="_blank" title="第24话" style="display: block;"><li>第24话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/bc133506-0772-11ed-8b3f-024352452ce0" target="_blank" title="七夕短篇" style="display: block;"><li>七夕短篇</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/c1c356de-0772-11ed-8b3f-024352452ce0" target="_blank" title="夏日短篇" style="display: block;"><li>夏日短篇</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/c564059a-0772-11ed-8b3f-024352452ce0" target="_blank" title="第25话" style="display: block;"><li>第25话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/7db1fef2-4f69-11ed-8a94-024352452ce0" target="_blank" title="第26话" style="display: block;"><li>第26话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/e386e92c-6369-11ed-a13f-024352452ce0" target="_blank" title="第27话" style="display: block;"><li>第27话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/abe29c28-8399-11ed-84f8-024352452ce0" target="_blank" title="第28话" style="display: block;"><li>第28话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/de56fa76-ff0b-11ed-a632-d3d228a76de6" target="_blank" title="第29话" style="display: block;"><li>第29话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/e03d7134-e354-11ee-8816-55b00c27fb36" target="_blank" title="第30话" style="display: block;"><li>第30话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/c8753264-e9fb-11ee-8c0a-55b00c27fb36" target="_blank" title="冬天款" style="display: block;"><li>冬天款</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/6d720156-f826-11ee-9364-69ffca9e099a" target="_blank" title="第31话" style="display: block;"><li>第31话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/4a89b5b9-f88e-11ee-937e-69ffca9e099a" target="_blank" title="童话旗袍" style="display: block;"><li>童话旗袍</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/a923235e-fff3-11ee-832b-3f487b7d9a9a" target="_blank" title="居家服" style="display: block;"><li>居家服</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/af1d057c-fff3-11ee-832b-3f487b7d9a9a" target="_blank" title="第32话" style="display: block;"><li>第32话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/1d5d81fe-0c30-11ef-858c-3f487b7d9a9a" target="_blank" title="第33话" style="display: block;"><li>第33话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/21e689dc-0c30-11ef-858c-3f487b7d9a9a" target="_blank" title="赏花" style="display: block;"><li>赏花</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/5d4a8244-6dec-11ef-b191-3f487b7d9a9a" target="_blank" title="夏装" style="display: block;"><li>夏装</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/932e0c88-7db3-11ef-b8ce-3f487b7d9a9a" target="_blank" title="第34话" style="display: block;"><li>第34话</li></a><a href="/comic/tonghuabandenikaishiliaolianaimenggong/chapter/d328cf3c-888d-11ef-bdcb-3f487b7d9a9a" target="_blank" title="第35话" style="display: block;"><li>第35话</li></a></ul>'

s = soup(str_c, features='lxml')

l = []
for i in s.find_all('a'):
    url = host_c+i.get('href')
    # T = 0
    # while T<5:
    #     try:
    #         getImg(url)
    #         break
    #     except Exception as e:
    #         T += 1
    #         print(e)
    #         time.sleep(1)
    l.append(i.text)

from PIL import Image
import os
from z2bookobj import usrEpubBook

def resize_p(picpath, optpath):
    image = Image.open(picpath)

    # 调整图像大小为宽度为 500 像素，高度按比例缩放
    resized_image = image.resize((800, int(image.size[1] * 800 / image.size[0])))
    resized_image.save(optpath)



bookname = '童話般的你開始了戀愛猛攻'
t = []
for i in l:
    t2 = []
    for j in range(len(os.listdir(f'{bookname}/{i}'))):
        t2.append(f'{j}.jpg')
    t.append((f'{i}', t2))

# for i in t:
#     if os.path.exists(f'.chche/{bookname}/{i[0]}'):
#         pass
#     else:
#         os.makedirs(f'.chche/{bookname}/{i[0]}')
#     for j in i[1]:
#         resize_p(f'{bookname}/{i[0]}/{j}', f'.chche/{bookname}/{i[0]}/{j}')

cover = 'cover.jpg'

# resize_p(f'{cover}', f'.chche/{cover}')

cover = f'.chche/{cover}'

usrEpubBook(t, f'.chche/{bookname}', cover)