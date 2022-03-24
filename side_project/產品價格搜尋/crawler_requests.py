import requests
import urllib3
import pandas as pd
import json

urllib3.disable_warnings()

url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E5%B0%BF%E5%B8%83&page=1&sort=sale/dc'

header={
'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}

# with open('./ip_data.csv','r',newline='',encoding='utf-8-sig') as f:
#     rows = pd.read_csv(f)
#     print(rows)

ip_url_next = '24.165.144.126:8080'


proxies = {'https': f'http://{ip_url_next}'}

response = requests.get(url,headers=header , proxies=proxies, verify=False)
datas = response.json()
print(datas['prods'])

    