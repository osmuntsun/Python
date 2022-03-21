# TQC+ 程式語言Python 610 平均溫度
# 設計說明：
# 請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
# 提示1：平均溫度輸出到小數點後第二位。
# 提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。

list_week=[]
for i in range(4):
    print("第 %d 周:"%(i+1))
    for j in range(3):
        digital_input=eval(input("第%d天:"%(j+1)))
        list_week.append(digital_input)
sum_total=0
for k in range(len(list_week)):
    sum_total+=list_week[k]
highest=max(list_week)
lowest=min(list_week)
average=sum_total/(len(list_week))
print("平均:%.2f\n最高溫:%.1f\n最低溫:%.1f"%(average,highest,lowest))

# L=[]
# for w in range(1,4+1):
#   print("Week %d:"%w)
#   for D in range(1,3+1):
#     x=eval(input("Day %d:"%D))
#     L.append(x)
 
# A=sum(L)/len(L)
# print("Average: %.2f"%A)
# print("Highest:",max(L))
# print("Lowest:",min(L))

# 輸入輸出：
# 輸入說明
# 四週各三天的溫度
# 輸出說明
# 平均溫度
# 最高溫度
# 最低溫度
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# 下圖中的 粉紅色點 為 空格