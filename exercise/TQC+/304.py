# TQC+ 程式語言Python 304 迴圈倍數總和
# 設計說明：
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和。

x=eval(input("輸入一個數："))
sum=0
for i in range(1,x+1):
    if i%5==0:
        sum+=i
print(sum)


# 輸入輸出：
# 輸入說明
# 一個正整數
# 輸出說明
# 所有5之倍數數字總和
# 輸入輸出範例
# 範例輸入
# 21
# 範例輸出
# 50