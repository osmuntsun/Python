import urllib.request as req
def getdata(url):
    urls='%s'%url
    #附加Request Headers的資訊
    requests =req.Request(urls,headers={
        'Cookie':'over18=1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        })
    with req.urlopen(requests) as response:
        data=response.read().decode('utf-8')

    import bs4
    root = bs4.BeautifulSoup(data,'html.parser')
    titles=root.find_all('div',class_='title') #尋找class='title'的DIV標籤
    #印出資料
    for title in titles:
        if title.a != None: #如果標題包含A標籤(沒有被刪除)就印出來
            print(title.a.string)
        else:
            print("None")
    nexttext = root.find('a',string='‹ 上頁')
    return nexttext['href']

pageurl='https://www.ptt.cc/bbs/Gossiping/index.html'
count=0
while count<5:
    pageurl='https://www.ptt.cc'+getdata(pageurl)
    count+=1
