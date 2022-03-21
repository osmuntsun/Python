# TQC+ 程式語言Python 503 連加計算
# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和。

def compute(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return print(sum)
a=eval(input("1:"))
b=eval(input("2:"))
compute(a,b)


# 輸入輸出：
# 輸入說明
# 兩個整數
# 輸出說明
# 從a連加到b的和
# 輸入輸出範例
# 範例輸入
# 33
# 66
# 範例輸出
# 1683