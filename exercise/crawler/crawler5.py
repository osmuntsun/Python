import pandas as pd
import urllib.request as req
import requests
import json
import bs4
url=requests.get('https://isin.twse.com.tw/isin/class_main.jsp?owncode=&stockname=&isincode=&market=2&issuetype=4&industry_code=34&Page=1&chklike=Y',headers={
        'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    })
list_pd=pd.read_html(url.text)[0]
del_list = list_pd.drop([0,1,4,5,6,8,9],axis=1)
del_list.columns=del_list.iloc[0]
df1=del_list[1:]

df1.to_excel('D:\我的文件夾\桌面\python-crawler\報表.xlsx',sheet_name=0,index=False,header=True)