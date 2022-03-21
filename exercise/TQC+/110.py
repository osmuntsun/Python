# 110_正n邊形面積計算

# 題目說明:

# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）
# 提示：
# -> 建議使用import math模組的math.pow及math.tan
# -> 正五邊形面積的公式：
# Area=(n∗s2)/(4∗tan(pi/n))
# -> 輸出浮點數到小數點後第四位

import math as MA



x=eval(input("輸入1值："))
y=eval(input("輸入2值："))

area=(x*(y**2)/(4*MA.tan(MA.pi/x)))

print("{:.4f}".format(area))



# 範例輸入1
# 8
# 6
# 範例輸出1

# Area = 173.8234