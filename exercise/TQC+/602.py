# TQC+ 程式語言Python 602 撲克牌總和
# 設計說明：
# 請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。
# 提示：J、Q、K以及A分別代表11、12、13以及1。

POKE_list=[]
total=0
for i in range(5):
    POKE=input("輸入第%d張牌"%(i+1))
    POKE_list.append(POKE)
for j in range(len(POKE_list)):
    if POKE_list[j]=="J":
        total+=11
    elif POKE_list[j]=="Q":
        total+=12
    elif POKE_list[j]=="K":
        total+=13
    elif POKE_list[j]=="A":
        total+=1
    else:
        total+=int(POKE_list[j])
print(total)

# 輸入輸出：
# 輸入說明
# 5張牌數
# 輸出說明
# 5張牌的數值總和
# 輸入輸出範例
# 範例輸入
# 5
# 10
# K
# 3
# A
# 範例輸出
# 32