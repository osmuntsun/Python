# 105_矩形面積計算

# 題目說明:

# 請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）


# 提示: 輸出浮點數到小數點後第二位

height=float(input("輸入高："))
width=float(input("輸入寬："))

perime=(height*2)+(width*2)
area=height*width
print("高：{:.2f}\n寬：{:.2f}\n周長：{:.2f}\n面積：{:.2f}".format(height,width,perime,area))


# 範例輸入1

# 23.5
# 19
# 範例輸出1

# Height = 23.50
# Width = 19.00
# Perimeter = 85.00
# Area = 446.50