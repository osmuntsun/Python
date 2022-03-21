# while 迴圈
# n=1
# sum=0   #記錄累加的結果
# while n<=10:
#    sum=sum+n
#    n+=1
# print(sum)

# for迴圈
# x=0
# for i in range(5,20):
#    x=x+i
# print(x)

# break簡易範例
# i=0
# while i<=5:
#     if i == 3:
#         break
#     i+=1
#     print(i)
# print("最後的:",i)

# continue簡易範例
# n=0
# for x in [0,1,2,3,4,5]: #<-只能字串或是列表
#     if x%2==0:
#         print(x)
#         continue    #<-跳過
#     print("沒有跳過的:",x)
#     n+=1
# print("最後的：",n)

# else範例
# i=0
# for x in range(11):
#     i+=x
# else:
#     print(i)

# 找出平方根
# 輸入9,得到3
# 輸入11,得到【沒有】整數的平方根
# i=int(input("請輸入數字："))
# for x in range(i+1):
#     if x*x==i:
#         print("開根號：",x)
#         break
# else:   #<---注意縮排 他是跟著FOR不是if
#     print("沒有")