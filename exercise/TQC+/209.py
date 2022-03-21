# 209_距離判斷

# 題目說明:

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，判斷此點是否與點(5, 6)的距離小於或等於15，如距離小於或等於15顯示【Inside】，反之顯示【Outside】

# 提示: 計算平面上兩點距離的公式：
#√(x1−x2)2+(y1−y2)2

import math as MA

x=eval(input("輸入X:"))
y=eval(input("輸入Y:"))

z=MA.sqrt((x-5)**2+(y-6)**2)

if z<=15:
    print("Inside")
else:
    print("Outside")
# 範例輸入1

# 7
# 20
# 範例輸出1

# Inside
# 範例輸入2

# 30
# 35
# 範例輸出2

# Outside

# 1.计算乘方

# pow(4,3)
# # 结果64

# 2.计算平方
# import numpy
# numpy.square(4)
# # 结果16
# pow(5,2)
# #结果25

# 3.平方根
# import numpy
# numpy.sqrt(16)
# # 结果4.0
# numpy.sqrt(16.)
# # 结果4.0
# pow(25, 0.5)
# #结果5.0
# pow(25, .5)
# #结果5.0
# import math
# math.sqrt(25)
# #结果5.0
# math.sqrt(25.0)
# #结果5.0
