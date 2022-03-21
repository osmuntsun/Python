import json
import urllib.request as req
#抓取資料
url='https://www.ptt.cc/bbs/movie/index.html'
request=req.Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
})
with req.urlopen(request) as response:
    data=response.read().decode('utf-8')
#解析資料
import bs4
root=bs4.BeautifulSoup(data,'html.parser') #讓beautifulsoup協助我們解析HTML格式文件
titles=root.find_all('div',class_='title') #尋找class='title'的DIV標籤
#印出資料
for title in titles:
    if title.a != None: #如果標題包含A標籤(沒有被刪除)就印出來
        print(title.a.string)
    else:
        print("None")
