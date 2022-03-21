# 104_圓形面積計算

# 題目說明:

# 請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）
# 提示：

# ->需import math模組，並使用math.pi
# ->輸出浮點數到小數點後第二位

import math as MA

radius = float(input("輸入半徑："))
perim=(radius*2)*MA.pi
area=(radius*radius)*MA.pi
print("半徑：{:.2f}\n周長：{:.2f}\n面積：{:.2f}".format(radius,perim,area))




# 範例輸入1
 
# 10
# 範例輸出1

# Radius = 10.00
# Perimeter = 62.83
# Area = 314.16
# 範例輸入2

# 2.5
# 範例輸出2

# Radius = 2.50
# Perimeter = 15.71
# Area = 19.63