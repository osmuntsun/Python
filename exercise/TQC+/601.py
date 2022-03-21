# TQC+ 程式語言Python 601 偶數索引值加總
# 設計說明：
# 請撰寫一程式，利用一維串列存放使用者輸入的12個正整數（範圍1~99）。顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。
# 提示：輸出每一個數字欄寬設定為3，每3個一列，靠右對齊。

one_list=[]
sum=1
total=0

for i in range(0,12):
    one_int=eval(input("輸入第%d個數"%(i+1)))
    if one_int>0 and one_int<100:
        one_list.append(one_int)
    else:
        print("錯誤")
for j in range(0,len(one_list)):
    sum+=1
    print("{:>3d}".format(one_list[j]),end="")
    if sum%4==0:
        sum=1
        print()
    elif one_list[j] %2==0:
        total+=one_list[j]
print(total)
       
        
# 輸入輸出：
# 輸入說明
# 12個正整數（範圍1~99）
# 輸出說明
# 格式化輸出12個正整數
# 12個數字中，索引為偶數的數字相加總合
# 輸入輸出範例
# 範例輸入
# 56
# 45
# 43
# 22
# 3
# 1
# 39
# 20
# 93
# 18
# 44
# 83
# 範例輸出
#  56 45 43
#  22  3  1
#  39 20 93
#  18 44 83
# 278