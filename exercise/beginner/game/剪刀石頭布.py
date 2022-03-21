import random
import time
def mora():
    if o==1:
        i=int(input("\n請輸入你要出的 1.剪刀 2.石頭 3.布\n請輸入數字："))
        a=random.choice([1,2,3])
        time.sleep(2)
        if a==i:
            print("\n平手！！！")
            input("離開\n\n")
        elif i==1 and a==2:
            print("\n你輸了 哈哈哈哈哈")
            input("離開\n\n")
        elif i==1 and a==3:
            print("\n恭喜你贏了")
            input("離開\n\n")
        elif i==2 and a==1:
            print("\n恭喜你贏了")
            input("離開\n\n")
        elif i==2 and a==3:
            print("\n你輸了 哈哈哈哈哈")
            input("離開\n\n")
        elif i==3 and a==1:
            print("\n恭喜你贏了")
            input("離開\n\n")
        elif i==3 and a==2:
            print("\n你輸了 哈哈哈哈哈")
            input("離開\n\n")
    else:
        print("\n歡迎下次再來\n\n")
        exit
o=int(input("是否開始遊玩【剪刀石頭步】?\n1.是的\n2.不要\n請輸入數字："))
mora()
