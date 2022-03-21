import urllib.request as req
import bs4
from selenium import webdriver
import time
import os

chrome="C:\selenium_driver_chrome\chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web=webdriver.Chrome(chrome)
web.get("https://www.instagram.com/crown_du")
web.set_window_position(0,0) #瀏覽器位置
web.set_window_size(700,700) #瀏覽器大小
os=req.Request(web,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; fbm_124024574287414=base_domain=.instagram.com; csrftoken=CieFJ3FXtSmqWjEwy4mOGDIoQtDTeoml; ds_user_id=1926542376; sessionid=1926542376%3Akyi3ElA6W2nXUu%3A13; shbid=17721; shbts=1568207948.3081348; rur=VLL; urlgen="{\"61.228.6.63\": 3462}:1i8580:rCWY-WGZSuCW688N50HXgQTz9sU"'
})
time.sleep(5)

titles=root.find_all("img")
folder="./photo/"
if (os.path.exists(folder) == false ):
    os.makedirs(folder)
else:
    print("沒印到")

for index , item in x(titles):
    if (item and index < photolimit):
        html = requests.get(item.get("src"))
        img_name=folder+str(index+1)+".png"

        with open(img_name,"wb") as fi:
            fi.write(html.content)
            fi.flush()
        fi.close()
        print("第{}張".format(index+1))
        time.sleep(1)
print("Done")

