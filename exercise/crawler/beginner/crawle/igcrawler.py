from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

SON=input('尋找目標')

dri=webdriver.Chrome('C:/selenium_driver_chrome/chromedriver.exe') #
dri.get("https://www.instagram.com/?hl=zh-tw")

time.sleep(3)
FB_login=dri.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[1]/div/form/div[1]/button/span').click()

email=dri.find_element_by_name('email')
email.send_keys('osmuntsun900606@gmail.com')

pas=dri.find_element_by_name('pass')
pas.send_keys('aa654321')

login=dri.find_element_by_name('login').click()
time.sleep(3)
after=dri.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()

sear=dri.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
sear.send_keys(SON)
time.sleep(1.5)
sea=dri.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()

url_set=set([])
pic_index=0
url_set_size=0
save_div='./pic/'
while True:
    dive=dri.find_elements_by_class_name('Nnq7C.weEfm')
    for i in dive:
        url_set.add(i.find_element_by_tag_name('a').get_attribute('href'))
        print(i.text)
    if len(url_set)==url_set_size:
        break
    url_set_size=len(url_set)
    ActionChains(dri).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(dri).send_keys(Keys.PAGE_DOWN).perform()
    ActionChains(dri).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(3)


