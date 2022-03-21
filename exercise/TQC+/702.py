# TQC+ 程式語言Python 702 數組合併排序
# 設計說明：
# 請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。

one_list_total=[]
two_list_total=[]
print("第一個串列")
while True:
    one_digital_input=eval(input())
    if one_digital_input!=-9999:
        one_list_total.append(one_digital_input)
    else:
        break
print("第二個串列")
while True:
    two_digital_input=eval(input())
    if two_digital_input!=-9999:
        two_list_total.append(two_digital_input)
    else:
        break
for i in range(len(two_list_total)):
    one_list_total.append(two_list_total[i])
new_list=sorted(one_list_total,reverse=False)
print(tuple(one_list_total))
print(new_list)

# N=0
# N2=0
# L1,L2=[],[]
# print('Create tuple1:')
# while(N!=-9999):
#   N=eval(input())
#   if N!=-9999:
#     L1.append(N)
# T1=tuple(L1)
 
# print('Create tuple2:')
# while(N2!=-9999):
#   N2=eval(input())
#   if N2!=-9999:
#     L2.append(N2)
 
# T2=tuple(L2)
 
# print('Combined tuple before sorting:', T1+T2)
# print('Combined list after sorting:', sorted(T1+T2))

# 輸入輸出：
# 輸入說明
# 兩個數組，直至-9999結束輸入
# 輸出說明
# 排序前的數組
# 排序後的串列
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Create tuple1:
# 9
# 0
# -1
# 3
# 8
# -9999
# Create tuple2:
# 28
# 16
# 39
# 56
# 78
# 88
# -9999
# Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
# Combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]