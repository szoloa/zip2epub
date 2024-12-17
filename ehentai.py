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
