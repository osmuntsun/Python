# TQC+ 程式語言Python 609 矩陣相加
# 設計說明：
# 請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。

x=[]
y=[]
for z in range(2):
    for i in range(2):
        for j in range(2):
            if z==0:
                digital_input=eval(input("[%d,%d]"%(i+1,j+1)))
                x.append(digital_input)
            elif z==1:
                digital_input=eval(input("[%d,%d]"%(i+1,j+1)))
                y.append(digital_input)
for k in range(4):
    if k==0:
        print("**%d %d **\n**%d %d **"%(x[k],x[k+1],x[k+2],x[k+3]))
    elif k==1:
        print("**%d %d **\n**%d %d **"%(y[k-1],y[k],y[k+1],y[k+2]))
    elif k==2:
        print("**%d %d **\n**%d %d **"%(x[k-2]+y[k-2],x[k-1]+y[k-1],x[k]+y[k],x[k+1]+y[k+1]))
    else:
        break

# L1 = [[0 for i in range(2)] for j in range(2)]
# L2 = [[0 for i in range(2)] for j in range(2)]
 
# print('Enter matrix 1:')
# for i in range(2):
#     for j in range(2):
#         L1[i][j] = int(input('[%d, %d]: '%(i+1,j+1)))
 
# print('Enter matrix 2:')
# for i in range(2):
#     for j in range(2):
#         L2[i][j] = int(input('[%d, %d]: '%(i+1,j+1)))
 
# print('Matrix 1:')
# for i in range(2):
#     for j in range(2):
#       print(L1[i][j],end=' ')
#     print()
 
# print('Matrix 2:')
# for i in range(2):
#     for j in range(2):
#       print(L2[i][j],end=' ')
#     print()
 
# print('Sum of 2 matrices:')
# for i in range(2):
#     for j in range(2):
#       print((L1[i][j]+L2[i][j]),end=' ')
#     print()
        

# 輸入輸出：
# 輸入說明
# 兩個2*2矩陣，皆輸入整數
# 輸出說明
# 矩陣1的內容
# 矩陣2的內容
# 矩陣1及矩陣2相加的結果
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Enter matrix 1:
# [1, 1]: 3
# [1, 2]: 5
# [2, 1]: 7
# [2, 2]: 5
# Enter matrix 2:
# [1, 1]: 6
# [1, 2]: 9
# [2, 1]: 8
# [2, 2]: 3
# Matrix 1:
# **3 5 **
# **7 5 **
# Matrix 2:
# **6 9 **
# **8 3 **
# Sum of 2 matrices:
# **9 14 **
# **15 8 **
