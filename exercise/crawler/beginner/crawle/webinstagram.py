from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#開啟的程式
dri = webdriver.Chrome('C:/selenium_driver_chrome/chromedriver.exe')
#開啟的網頁
dri.get('https://www.google.com')

#尋找需要的東西
q=dri.find_element_by_name('q')
#輸入內容
q.send_keys('大數軟體')
#回傳
q.send_keys(Keys.RETURN)
#解析
soup=BeautifulSoup(dri.page_source,'lxml')
#把標題取下來
for ele in soup.select('#rso h3 div'):
    print(ele.text)
#下一頁
dri.find_element_by_link_text('下一頁').click()
#點三次下一頁然後把標題取下
for q in range(3):
    dri.find_element_by_link_text('下一頁').click()
    soup=BeautifulSoup(dri.page_source,'lxml')
    for ele in soup.select('#rso h3 div'):
        print(ele.text)
    #休息三秒
    time.sleep(3)