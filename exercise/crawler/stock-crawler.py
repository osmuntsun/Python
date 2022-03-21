import urllib.request as req
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup

# start = dt.datetime(2021,1,1)
# end = dt.datetime(2021,3,10)

url = 'https://stock.wearn.com/cdata.asp?Year=110&month=04&kind=2330'


requests = req.Request(url,headers={
        'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    })

with req.urlopen(requests) as response:
    data = response.read()


soup = BeautifulSoup(data,'html.parser')

date1 = soup.find_all('td',align='right')
date2 = soup.find_all('td',align='center')

date = []
for i in date2:
    date.append(i.text)

sum=4
list_data = []
for i in date1:
    sum+=1
    if sum==5:
        list_data.append(eval(i.text.replace('.00\xa0\xa0\xa0','')))
        sum=0


plt.plot(date,list_data,'r--.')
plt.xticks(rotation=45) #設定x軸刻度
plt.title('opening price',fontsize=25)

plt.show()