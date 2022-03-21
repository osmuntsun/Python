# TQC+ 程式語言Python 604 眾數
# 設計說明：
# 請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。

count=0
count_digital=0
total_list=[]
for i in range(10):
    digital_input=eval(input("輸入第%d次:"%(i+1)))
    total_list.append(digital_input)
for j in range(len(total_list)):
    if total_list.count(total_list[j])>count:
        count=total_list.count(total_list[j])
        count_digital=total_list[j]
print(count_digital)
print(count)



# 提示：假設樣本中只有一個眾數。
# 輸入輸出：
# 輸入說明
# 十個整數
# 輸出說明
# 眾數
# 眾數出現的次數
# 輸入輸出範例
# 範例輸入
# 34
# 18
# 22
# 32
# 18
# 29
# 30
# 38
# 42
# 18
# 範例輸出
# 18
# 3