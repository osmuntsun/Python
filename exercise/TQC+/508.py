# TQC+ 程式語言Python 508 最大公因數
# 設計說明：
# 請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。

def compute(x,y):
  for i in range(1,little+1):
    if x%i==0 and y%i==0:
      L1.append(i)
  return max(L1)
 
L1=[]
x=eval(input())
y=eval(input())
little=min(x,y)
print(compute(x,y))

# 輸入輸出：
# 輸入說明
# 兩個正整數（以半形逗號分隔）
# x,y
# 輸出說明
# 最大公因數
# 輸入輸出範例
# 範例輸入1
# 12,8
# 範例輸出1
# 4
# 範例輸入2
# 4,6
# 範例輸出2
# 2