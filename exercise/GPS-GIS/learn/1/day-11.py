import requests
import pandas as pd
import geopandas as gpd
import re 
from bs4 import BeautifulSoup
from shapely.geometry import Point

result = requests.get(
    'https://news.ftv.com.tw/AMP/News_Amp.aspx?id=2018A25W0003')
print(result.text)
soup = BeautifulSoup(result.text, 'html.parser')

p_count=0
start_flag=False
p_contents=soup.find_all('p')
all_data=[]
location=""
time=""
for p_item in p_contents:
    
    text=str(p_item.text)
    if text =='完整通聯紀錄：':
        start_flag=True
        p_count+=1
        continue
    
    if len(re.findall('地點',text))>0:
        location=text
        continue
        
    if len(text.split(':'))==3 and len(text)==8:
        time=text
        continue
            
    # 處理前幾行
    if start_flag==True:
        if  p_count<4:
            p_count+=1
            time=text[0:8]
            all_data.append([location,time,text[8:]])
        else:
            all_data.append([location,time,text])

print(all_data)


