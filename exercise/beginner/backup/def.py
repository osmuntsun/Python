# #定義並呼叫函式
# def i(n1,n2): #<--(2.)n1,n2變成5,9
#     a=(n1+n2)//2 #<--(3.)算出結果 a變成結果
#     return a  #<--(4.)回傳a這個數值
# s=i(5,9) #<--(1.)i先呼叫函式 #(6.)s=變成a回傳的數值
# print(s)#<--輸出S

#定義函式
#函式內部的程式碼沒有呼叫就不會執行
# def multiply(n1,n2):
#     print(n1*n2)
# x1=int(input("輸入一:"))
# x2=int(input("輸入二:"))
# q=multiply(x1,x2)
# print(q)

#程式的包裝
# def o(a):
#     n=0
#     for i in range(a+1):
#         n=n+i
#     print(n)
#     return n
#     print(n)
# a=int(input("請輸入:"))
# o1=o(a)
# o2=o(10)
# o3=o1+o2
# print(o3)

#def的應用
# def i(n1,n2):
#     a=n1/n2
# i(2,4)#印出0.5
# i(n2=2,n1=4)#印出2

#無限/不定長度的參數
#def 函式名稱(*無限參數):
    #以Tuple的方式處理
#變數("","","")<-可以無限

#參數的預設資料
# def i(n1,n2=0):
#     print(n1**n2)
# i(3,2)
# i(3)

#參數的指定名稱
# def i(n1,n2):
#     print(n1//n2)
# i(2,4)
# i(n2=2,n1=4)

# def i(*n1):
#     w=0
#     for a in n1:
#         w=w+a
#     print(w/len(n1)) #<--len是判斷字串的長度
# i(3,4)
# i(3,4,5,6)
# i(3,4,5,6,7,8,9)