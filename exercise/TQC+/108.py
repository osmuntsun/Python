# 108_座標距離計算

# 題目說明:


# 請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離
# 提示：

# ->歐式距離 = sqrt((x1 - x2)^2+(y1 - y2)^2)就是=> 
   
# -> 兩座標的歐式距離，輸出到小數點後第4位 

import math as MA

a=eval(input("x1："))
b=eval(input("y1："))
c=eval(input("x2："))
d=eval(input("y2："))

x=MA.sqrt((a-c)**2+(b-d)**2)

print("( {} , {} )".format(a,b))
print("( {} , {} )".format(c,d))
print("歐式距離：{:.4f}".format(x))


# 範例輸入1

# 2
# 1
# 5.5
# 8
# 範例輸出1

# ( 2 , 1 )
# ( 5.5 , 8 )
# Distance = 7.8262
# 範例輸入2

# 2.5
# 範例輸出2

# Radius = 2.50
# Perimeter = 15.71
# Area = 19.63