# TQC+ 程式語言Python 306 迴圈階乘計算
# 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。

x=eval(input("輸入一數："))
sum=1
for i in range(1,x+1):
    sum*=i
print(sum)





# 輸入輸出：
# 輸入說明
# 一個正整數
# 輸出說明
# 計算n!的值
# 輸入輸出範例
# 範例輸入
# 15
# 範例輸出
# 1307674368000