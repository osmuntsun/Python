import requests
import pandas as pd
from openpyxl.workbook import Workbook

city=['基隆市','臺北市','新北市','桃園市','新竹市','新竹縣','苗栗縣','台中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','台南市','高雄市','屏東縣','花蓮縣','台東縣','澎湖縣','金門縣','連江縣','南海諸島']

for index , city in enumerate(city):
    data={'strTargetField':'COUNTY','strKeyWords':'{}'.format(city)}
    res=requests.post("http://www.ibon.com.tw/retail_inquiry_ajax.aspx",data=data)
    if index == 0:
        df_711_store=pd.read_html(res.text,header=0)[0]
        df_711_store['縣市']=city
    if index > 0:
        df_711_store_=pd.read_html(res.text,header=0)[0]
        df_711_store_['縣市']=city
        df_711_store=df_711_store.append(df_711_store_)
    # print('%2d %-s %4d' %(index+1,5,city,pd.read_html(res.text,header=0)[0].shape[0]))
df_711_store.to_excel('E2-1-2-1-output.xlsx',encoding='utf-8',index=False)
