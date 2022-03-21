import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

df=pd.read_csv('try.csv')
print(df)
# df.dropna() 刪除空白
# df.fillna(1234567) 補空白的值

x = list(df['team'])
y = list(df['bobo'])
plt.figure(figsize=(10,5))
print(y,x)
plt.bar(x,y,label='smallcar')
plt.show()




# 開啟 CSV 檔案
# color_list=['red','green','blue','white','black','yellow']
# x_lable=[]
# y_lable=[]
# with open('try.csv',newline='', encoding='utf-8') as f:
#     myCsv = csv.reader(f)
#     headers = next(myCsv)
#     for row in myCsv:
#         if row == row:
#             x_lable.append(row[0])
#             y_lable.append(row[1])
#             continue

# print(x_lable,y_lable)
# x = np.linspace(0,10000,10)
# plt.ylim()
# plt.bar(x_lable,y_lable,align = "center")
# plt.show()






# 設定標籤
# plt.legend(plots, ('Apple', 'Facebook', 'Google'), loc='best', framealpha=0.5, prop={'size': 'large', 'family': 'monospace'})