# import requests
# from bs4 import BeautifulSoup as soup
# from io import BytesIO
# from PIL import Image

# import os

# from selenium.webdriver.chrome.options import Options
# from seleniumwire.webdriver import Chrome

# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium import webdriver

# from selenium.webdriver.common.by import By


# proxy = {
#     'http': 'http://127.0.0.1:7890', 
#     'https': 'http://127.0.0.1:7890', 
# }

# header = {
#     'referer' : 'https://e-hentai.org/',
# }

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# driver = webdriver.Chrome(service=ChromeService('/usr/bin/chromedriver'), options=chrome_options)

# def getPic(url, page):
#     url = f'{url}?p={page}'

#     r = requests.get(url, proxies=proxy)
#     s = soup(r.text, features='lxml')

#     t = s.find(id='gn').text.replace(' ', '_')
    
#     for i in s.find(id='gdt').find_all(class_='gdtm'):
#         driver.get(i.a.get('href'))
#         src=driver.find_element(By.ID, 'img').get_attribute('src')
#         tempIm = BytesIO(requests.get(src, proxies=proxy, headers=header).content)
#         im = Image.open(tempIm)
#         if not os.path.exists(f'{t}'):
#             os.mkdir(f'{t}')
#         im.save(f'{t}/{i.a.get('href').split('/')[-1]}.jpg')
#         print(i.a.get('href'))

# for i in range(2):
#     getPic('https://e-hentai.org/g/1803030/47ae95efc8/', i)












# for r in driver.iter_requests():
#     if r.url==src:
#         with open('img', 'wb') as f:
#             f.write(r.response.body)


# # import base64
# # import os
# # import re
# # from io import BytesIO
# # from PIL import Image

# # def base64_to_image(base64_str):
# #     base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
# #     byte_data = base64.b64decode(base64_data)
# #     image_data = BytesIO(byte_data)
# #     img = Image.open(image_data)
# #     return img


# # js = "let c = document.createElement('canvas');let ctx = c.getContext('2d');" \
# #      "let img = document.getElementsByTagName('img')[0]; /*找到图片*/ " \
# #      "c.height=img.naturalHeight;c.width=img.naturalWidth;" \
# #      "ctx.drawImage(img, 0, 0,img.naturalWidth, img.naturalHeight);" \
# #      "let base64String = c.toDataURL();return base64String;"
     
# # base64_str = driver.execute_script(js)
# # img = base64_to_image(base64_str)

# # img.save('xx.png')


import requests
from bs4 import BeautifulSoup as soup
from io import BytesIO
from PIL import Image
import os
import threading
import time

# 使用requests.Session来复用连接
session = requests.Session()
proxy = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
session.proxies.update(proxy)

header = {
    'referer': 'https://e-hentai.org/',
}
session.headers.update(header)

def create_folder(folder_name):
    """检查并创建文件夹"""
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def download_image(img_url, folder_name, img_name):
    """下载并保存图片"""
    if os.path.exists(os.path.join(folder_name, f'{img_name}.jpg')):
        print(f'{img_name}.jpg', 'passover')
        return
    t = 0
    while t < 5:
        try:
            response = session.get(img_url, timeout=10)
            temp_im = BytesIO(response.content)
            im = Image.open(temp_im)
            
            im.save(os.path.join(folder_name, f'{img_name}.jpg'))
            print(f"Downloaded: {img_name}")
            break
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            t += 1
            time.sleep(10)

def get_images_from_page(url, page):
    """解析页面并下载所有图片"""
    url = f'{url}?p={page}'
    r = session.get(url)
    s = soup(r.text, features='lxml')

    folder_name = s.find(id='gn').text.replace(' ', '_')
    create_folder(folder_name)

    # 使用并发下载图片
    threads = []
    for i in s.find(id='gdt').find_all(class_='gdtm'):
        img_page_url = i.a.get('href')
        img_page_soup = soup(session.get(img_page_url).text, 'lxml')
        img_src = img_page_soup.find(id='img').get('src')
        img_name = img_page_url.split('/')[-1]
        
        thread = threading.Thread(target=download_image, args=(img_src, folder_name, img_name))
        threads.append(thread)
        thread.start()

    # 等待所有线程结束
    for thread in threads:
        thread.join()

# 抓取多页
for i in range(1):
    get_images_from_page('https://e-hentai.org/g/3092246/cac77b9e69/', i)
