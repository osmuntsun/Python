import random
import time

# 初始本金是1000元，預設賠率是1倍，贏了，獲得一倍金額，輸了，扣除1倍金額。

# 玩家選擇下注，押大或押小；
# 輸入下注金額；
# 搖3個骰子，11≤骰子總數≤18為大，3≤骰子總數≤10為小；
# 如果贏了，獲得1倍金額，輸了，扣除1倍金額，本金為0時，遊戲結束。

bangmoney=1000
print("歡迎來到阿吉賭博場")
time.sleep=1.2
def star():
    print("-----即將開始-----\n")
    time.sleep=1.2
    print("----搖骰子聲----\n")
    time.sleep=2.5
    print("----搖骰子聲----\n")
    time.sleep=2.5
    print("----搖骰子聲----\n\n")
    time.sleep=2.5
    a1=[1,2,3,4,5,6]
    a2=[1,2,3,4,5,6]
    a3=[1,2,3,4,5,6]
while bangmoney>0:
    print("現在你身上有{}元".format(bangmoney))
    time.sleep=1
    A=int(input("請先決定要押大還是押小\n11以上(包含)是大 10以下(包含)是小\n1.押大\n2.押小\n請輸入數字："))
    time.sleep=1
    batmoney=int(input("\n輸入下注金額："))
    star()
    a1=random.choice([1,2,3,4,5,6])
    a2=random.choice([1,2,3,4,5,6])
    a3=random.choice([1,2,3,4,5,6])
    out=a1+a2+a3
    if out>=11 and A==1:
        bangmoney=bangmoney+batmoney
        print("恭喜你贏了{}元,現在你身上的金額有{}元\n\n".format(batmoney,bangmoney))
    elif out<=10 and A==2:
        bangmoney=bangmoney+batmoney
        print("恭喜你贏了{}元,現在你身上的金額有{}\n\n".format(batmoney,bangmoney))
    else:
        bangmoney=bangmoney-batmoney
        print("可惜你輸了{}元,現在你身上的金額有{}\n\n".format(batmoney,bangmoney))
    x=int(input("要繼續嗎?\n1.繼續押阿\n2.離開\n請輸入數字："))
    if x==2:
        print("\n\n謝謝光臨你現在身上的錢有{}元".format(bangmoney))
        time.sleep=2
        bangmoney=-1000
        exit