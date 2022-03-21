# 204_算術運算

# 題目說明:

# 請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果

x=eval(input("數值1:"))
y=eval(input("數值2:"))
z=str(input("輸入 + - * / // % : "))

if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    print(x/y)
elif z=="//":
    print(x//y)
elif z=="%":
    print(x%y)
else:
    print("請輸入指定字串")




# 範例輸入1

# 30
# 20
# *
# 範例輸出1

# 600