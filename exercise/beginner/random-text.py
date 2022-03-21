#隨機模組
import random
#隨機選取(單個)
# data=random.choice([1,4,6,89,765,4,435])
# print(data)
#隨機選取(多個)
# data=random.sample([1,2,5,8,4,2,3],3)
# print(data)

#隨機調換順序(洗牌的感覺)
# data=[1,5,7,2,3,5]
# random.shuffle(data)
# print(data)

#隨機取得亂數
# data=random.random() #0~1的隨機亂數
# print(data)
#--------------
# data=random.uniform(60,100) #指定數字之間的亂數
# print(data)

#常態分配亂數
#平均數100標準差10,得到的資料【多數】在90~110之間
# data=random.normalvariate(100,10)
# print(data)
#平均數 0 標準差5 得到的資料【多數】在-5~5之間
# data=random.normalvariate(0,5)
# print(data)

#統計模組
import statistics as stat
#平均數 mean
# data=stat.mean([1,2,3,4,5,8,100])
# print(data)
#中位數median
# data=stat.mean([1,2,3,4,5,8,100])
# print(data)
#標準差 stdev
# data=stat.stdev([1,2,3,4,5,8,100])
# print(data)