# TQC+ 程式語言Python 608 最大最小值索引
# 設計說明：
# 請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。

list_input=[]
list_total=[]
for i in range(3):
    for j in range(3):
        digital_input=eval(input("輸入數字:"))
        list_input.append(digital_input)
    list_total.append(list_input)
    list_input=[]
big_list=0
small_list=0
x1=0
x2=0
y1=0
y2=0
for x in range(len(list_total)):
    for y in range(len(list_total[x])):
        if list_total[x][y]>big_list:
            big_list=list_total[x][y]
            x1=x
            y1=y
        elif list_total[x][y]<small_list:
            small_list=list_total[x][y]
            x2=x
            y2=y
print("最大數是:%s(%s,%s)\n最小數是:%s(%s,%s)"%(big_list,x1,y1,small_list,x2,y2))

# L=[]
# for i in range(9):
#   L.append(int(input()))
 
# max_n=max(L)
# max_n_index=L.index(max_n)
 
# print("Index of the largest number {} is: ({}, {})"
#       .format(max_n,max_n_index//3,max_n_index%3))
 
# min_n=min(L)
# min_n_index=L.index(min_n)
 
# print("Index of the smallest number {} is: ({}, {})"
#       .format(min_n,min_n_index//3,min_n_index%3))

# 輸入輸出：
# 輸入說明
# 九個整數
# 輸出說明
# 矩陣最大值及其索引
# 矩陣最小值及其索引
# 輸入輸出範例
# 範例輸入
# 6
# 4
# 8
# 39
# 12
# 3
# -3
# 49
# 33
# 範例輸出
# Index of the largest number 49 is: (2, 1)
# Index of the smallest number -3 is: (2, 0)