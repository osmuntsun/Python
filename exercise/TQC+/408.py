# TQC+ 程式語言Python 408 奇偶數個數計算
# 設計說明：
# 請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

one=0
two=0
j=1
while True:
    if j==11:
        break
    x=eval(input("輸入第%d個整數"%j))
    if x%2==0:
        two+=1
    else:
        one+=1
    j+=1
print("奇數有%d個\n偶數有%d個"%(one,two))

# 輸入輸出：
# 輸入說明
# 十個整數
# 輸出說明
# 偶數的個數
# 奇數的個數
# 輸入輸出範例
# 範例輸入
# 69
# 48
# 19
# 91
# 83
# 22
# 18
# 37
# 82
# 40
# 範例輸出
# Even numbers: 5
# Odd numbers: 5