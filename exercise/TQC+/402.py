# TQC+ 程式語言Python 402 不定數迴圈-最小值
# 設計說明：
# 請撰寫一程式，讓使用者輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。

l=[]

while True:
    x=eval(input(".:"))
    if x==9999:
        break
    l.append(x)
print(min(l))



# 輸入輸出：
# 輸入說明
# n個數值，直至9999結束輸入
# 輸出說明
# n個數值中的最小值
# 輸入輸出範例
# 範例輸入
# 29
# 100
# 948
# 377
# -28
# 0
# -388
# 9999
# 範例輸出
# -388