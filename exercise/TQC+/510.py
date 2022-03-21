# TQC+ 程式語言Python 510 費氏數列
# 設計說明：
# 請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，
# 並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。
# 提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：

def compute(x):
    j=[0,1]
    for i in range(x):
        if i == 0:
            print(i,end=" ")
        elif i == 1:
            print(i,end=" ")
        elif i>=2:
            j.append(j[i-1]+j[i-2])
            print(j[i],end=" ")
            
num=eval(input("輸入大於二："))
compute(num)

# 輸入輸出：
# 輸入說明
# 一個正整數num (num>=2)
# 輸出說明
# 依輸入值num，輸出費氏數列前num個的數值（每個數值後方為一個半形空格）
# 輸入輸出範例
# 範例輸入1
# 10
# 範例輸出1
# 0 1 1 2 3 5 8 13 21 34 
# 範例輸入2
# 20
# 範例輸出2
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181