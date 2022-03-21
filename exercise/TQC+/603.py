# TQC+ 程式語言Python 603 數字排序
# 設計說明：
# 請撰寫一程式，要求使用者輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。

ten_list=[]
big_list=[]
mitime=0
for i in range(10):
    user_input=eval(input('輸入第%d個數字'%(i+1)))
    ten_list.append(user_input)
for j in range(len(ten_list)):
    if mitime==3:
        break
    else:
        mitime+=1
        big_list.append(max(ten_list))
        ten_list.remove(max(ten_list))
print(big_list)


# 輸入輸出：
# 輸入說明
# 十個數字
# 輸出說明
# 由大到小排序，顯示最大的3個數字
# 輸入輸出範例
# 範例輸入1
# 40
# 32
# 12
# 29
# 20
# 19
# 38
# 48
# 57
# 44
# 範例輸出1
# 57 48 44
# 範例輸入2
# 139
# 246
# 15
# 38
# 77
# 122
# 42
# 30
# 100
# 1
# 範例輸出2
# 246 139 122