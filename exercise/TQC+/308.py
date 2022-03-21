# TQC+ 程式語言Python 308 迴圈位數加總
# 設計說明：
# 請使用迴圈敘述撰寫一程式，要求使用者輸入一個數字，此數字代表後面測試資料的數量。
# 每一筆測試資料是一個正整數（由使用者輸入），將此正整數的每位數全部加總起來。

n=eval(input("輸入需要加總的數目："))
for i in range(n):
    sn=input("第{}筆項目：".format(i+1))
    ALL=0
    for j in range(len(sn)):
        ALL+=int(sn[j])
    print("共",sn,"筆項目\n加總後為",ALL)




# 輸入輸出：
# 輸入說明
# 先輸入一個正整數代表後面測試資料的數量
# 依測試資料的數量，再輸入正整數的測試資料
# 輸出說明
# 將測試資料的每位數全部加總
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示 1
# 1
# 98765
# Sum of all digits of 98765 is 35
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示 2
# 3
# 32412
# Sum of all digits of 32412 is 12
# 0
# Sum of all digits of 0 is 0
# 769
# Sum of all digits of 769 is 22