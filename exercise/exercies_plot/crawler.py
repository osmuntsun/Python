# 引進相關套件
import requests
from io import StringIO
import pandas as pd
import numpy as np

# 資料日期
date1 = '20201120'
stockNo = '2330'

# 網址
url= 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date={}&stockNo={}'.format(date1, stockNo)

# 送出要求，並取得回應資料
response = requests.post(url)

clean_data=[]
for row in response.text.split('\n'):
    fields=row.split('",')
    if len(fields) == 10 and row[0] != '=':
        clean_data.append(row.replace(' ',''))

csv_data = "\n".join(clean_data)
print(csv_data)

df = pd.read_csv(StringIO(csv_data))
df.head()

# 刪除無用的欄位
df.drop(df.columns[-1], axis=1, inplace=True)

# 將以下欄位轉為數值
numeric_columns=['成交股數','成交金額','成交筆數']
for i in numeric_columns:
    df[i]=df[i].map(lambda x:x.replace(',', '').replace('--', ''))
    df[i]=pd.to_numeric(df[i])
df.info()

df.to_csv('個股日成交資訊.csv', index=False)

df.to_excel('個股日成交資訊.xlsx', index=False)

df = pd.read_excel('個股日成交資訊.xlsx')

df['日期1']=df['日期'].str.slice(start=-2)
df['日期1']

import matplotlib.pyplot as plt
plt.plot(df['日期1'], df['收盤價'])
