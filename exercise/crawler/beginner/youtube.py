import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import os

print("HI")
son=input("想聽的歌(YOUTUBE):")
dri=webdriver.Chrome("D:\我的文件夾\桌面\youtube\chromedriver.exe")
dri.get('https://www.youtube.com/?gl=TW&hl=zh-tw')

q=dri.find_element_by_name('search_query')
q.send_keys(son)
q.send_keys(Keys.RETURN)

time.sleep(3)
soup = BeautifulSoup(dri.page_source,'lxml')

hrefs=dri.find_element_by_xpath('//*[@id="video-title"][1]').click()

# xm=dri.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[1]/span/div')

# xm={'aria-valuenow':'name'}
# xm['aria-valuenow']='2'

mutitle=soup.find("yt-formatted-string",{"class":"style-scope ytd-video-primary-info-renderer"})
mutitle2=""
if mutitle != mutitle2:
    mutitle2 = mutitle
    print("播過歌曲：{}".format(mutitle))