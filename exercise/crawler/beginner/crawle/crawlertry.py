#抓取ptt電影版的網頁原始碼
sum=0
import urllib.request as req
for sum in range(1,2):
    su=str(sum)
    url=("https://www.ptt.cc/bbs/movie/index{}.html".format(su))
    #建立一個Request物件,附加Request Headers的資訊
    os=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    })
    with req.urlopen(os) as ren:
        data=ren.read().decode('utf-8')
    #解析原始碼,取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") #讓 Beautifulsoup 協助我們解析 HTML 格式文件
    #title抓標題 string取他裡面的字
    #print(root.title.string)
    #find只會找到其中一個 加上_all 取出全部的標籤
    titles=root.find_all('div',class_="title")#尋找 class="title" div 標籤
    #.a取出a標籤 string取裡面的標題
    # print(titles.a.string)
    for title in titles:
        if title.a != None: #如果標題包含 a 標籤 (沒有被刪除), 印出來
            with open('A.txt',mode='r+',encoding="utf-8") as open1:
                open1.write(title.a.string)
            print(title.a.string)
    