# 302_迴圈偶數連加

# 題目說明:

# 請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），利用迴圈計算從a開始的偶數連加到b的總和。
# 例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）

x=eval(input("輸入第一個數值："))
y=eval(input("輸入第二個數值："))

z=0
for i in range(x,y+1):
    if i%2==0:
        z+=i
print(z)

# 範例輸入1

# 14
# 1144
# 範例輸出1

# 327714