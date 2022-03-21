import requests
from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dri=webdriver.Chrome('C:/selenium_driver_chrome/chromedriver.exe')
dri.get('https://m.facebook.com/')

email=dri.find_element_by_name('email')
email.send_keys('osmuntsun900606@gmail.com')

password=dri.find_element_by_name('pass')
password.send_keys("aa654321")

logi=dri.find_element_by_name('login')
logi.send_keys(Keys.RETURN)

Ok=dri.find_element_by_xpath('//*[@id="root"]/div[1]/div/div/div[3]/div[2]/form/div/button')
Ok.send_keys(Keys.RETURN)