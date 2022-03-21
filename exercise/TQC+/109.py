# 109_正五邊形面積計算

# 題目說明:

# 請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）
# 提示：

# -> 建議使用import math模組的math.pow及math.tan
# -> 正五邊形面積的公式：
# Area=(5∗s2)/(4∗tan(pi/5))

import math as MA

x=eval(input("輸入值："))
area=(5*(x**2)/(4*MA.tan(MA.pi/5)))
print("{:.4f}".format(area))

# -> 輸出浮點數到小數點後第四位
# 範例輸入1

# 5
# 範例輸出1

# Area = 43.0119