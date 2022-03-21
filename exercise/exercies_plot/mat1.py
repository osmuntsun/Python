import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

df = pd.read_csv('try2.csv')
print(df)
x = list(df['會員電話'])
y = list(df['套餐'])
a = list(df['一般水'])
z = list()
w = list()
digital = 1
for i in range(len(x)):
    z.append('%d'%digital)
    w.append('-%d'%digital)
    digital += 1
print(x,y,z)

plt.figure(figsize=(30,5))
plt.bar(z,y,alpha=0.9)
plt.grid(linestyle='--',axis='y') #<-- 設置格線
plt.plot(z,a,alpha=0.9,color='red')
plt.ylim(0,15)

plt.show()