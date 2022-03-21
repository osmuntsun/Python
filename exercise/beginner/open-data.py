#網路連線
# import urllib.request as req
# src="https://www.facebook.com/messages/t/100004093265019"
# with req.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得網頁的原始碼 (HTML.CSS.JS)
# print(data)

#串接、攝取公開資料
import urllib.request as req
import json
src="https://www.facebook.com/messages/t/100004093265019"
with req.urlopen(src) as response:
    data=json.load(response).decode("utf-8") #取得網頁的原始碼 (HTML.CSS.JS)
print(data)
#取得資料
