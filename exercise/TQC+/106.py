# 106_公里英哩換算

# 題目說明:

# 假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）

# 提示: 輸出浮點數到小數點後第一位

x=eval(input("幾分："))
y=eval(input("幾秒："))
z=eval(input("幾公里："))

tim=(x+y/60)/60
speed=(z/1.6)/tim

print("平均英哩速率：{:.1f}".format(speed))

# 範例輸入1

# 10
# 25
# 3
# 範例輸出1

# Speed = 10.8