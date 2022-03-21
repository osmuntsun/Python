import pandas as pd 

data=pd.Series([20, 10, 15]) # 要 列表 資料
# print(data)
# print(data.max())    #最大值
# print(data.median()) #中位數

#可以進行運算
# data1 = data*2  
# print(data1)

#可以進行判斷
# data=data==20  
# print(data)

# 建立 dataframe 要 字典 
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000, 50000, 40000]
})
# 基本 DataFrame 操作
print(data)
