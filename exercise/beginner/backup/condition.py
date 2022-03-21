#判斷式
#x=input("請輸入數字 :")
#x=int(x)
#if x>=200:
#    print("等於200或是大於200")
#elif x>100:
#    print("大於100 小於200")
#else:
#    print("小於100")

#四則運算
n1=int(input("請輸入數字一："))
n2=int(input("請輸入數字二："))
op=input("輸入運算：+,-,*,/：")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援的運算")