from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
import requests 

url = 'https://www.mangacopy.com/comic/tonghuabandenikaishiliaolianaimenggong'

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService('/usr/bin/chromedriver'),options=chrome_options)
driver.get(url)

time.sleep(2)

s = soup(driver.page_source, features='lxml')

print(s.find(class_='tab-pane fade show active').find_all('li'))

# x = [i.text[-1] for i in s.find(class_='page-all comic-detail-page').find_all(class_='page-total') if i.text[-1] in [str(i)for i in range(0, 20)]]

# print(int(x[0]))

