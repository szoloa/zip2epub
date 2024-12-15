from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
import requests
from PIL import Image
from io import BytesIO
import os

def getImg(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService('/usr/bin/chromedriver'), options=chrome_options)
    driver.get(url)
    time.sleep(2)
    temp_height = 0
    while True:
        driver.execute_script("window.scrollBy(0, 200)")
        time.sleep(0.01)
        check_height = driver.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        if check_height == temp_height:
            break
        temp_height = check_height
        print('\r翻页中：' + str(check_height), end='')
    print()
    st = soup(driver.page_source, features='lxml')
    f = st.find(class_='header').text.replace(' ', '_').split('/')
    if not os.path.exists(f[0]):
        os.mkdir(f[0])
    if not os.path.exists(f'{f[0]}/{f[1]}'):
        os.mkdir(f'{f[0]}/{f[1]}')
    if st.find(class_='comicContent-list comic-size-1'):
        t = st.find(class_='comicContent-list comic-size-1').find_all('li')
    elif st.find(class_='comicContent-list comic-size-2'):
        t = st.find(class_='comicContent-list comic-size-2').find_all('li')
    else:
        print('失败')
        return
    for i in range(len(t)):
        tp = 0
        if os.path.exists(f'{f[0]}/{f[1]}/{i}.jpg'):
            continue
        while tp < 10:
            try:
                yzmdata = requests.get(t[i].img.get('data-src'))
                break
            except Exception as e:
                time.sleep(1)
                tp += 1
        if tp >= 10:
            print('失败')
            continue
        tempIm = BytesIO(yzmdata.content)
        im = Image.open(tempIm)
        im.save(f'{f[0]}/{f[1]}/{i}.jpg')
        print(f'\r正在下载：第{i+1}页\\共{len(t)}页', end='')
    print()

if __name__ == '__main__':
    url = 'https://www.mangacopy.com/comic/tonghuabandenikaishiliaolianaimenggong/chapter/2f5bac20-e60c-11eb-9888-00163e0ca5bd'
    T = 0
    while T<5:
        try:
            getImg(url)
        except:
            T += 1
            time.sleep(1)
        break
