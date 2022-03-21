import requests
import json
import pandas as pd
import numpy as np

url="https://query1.finance.yahoo.com/v8/finance/chart/2353.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
requestsurl=requests.get(url,headers=headers)
data=json.loads(requestsurl.text)
df=pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))
print(df.head())

