# 201_偶數判斷

# 題目說明:

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）

x=eval(input("輸入值："))

if x%2 == 0:
    print("{} is an even number".format(x))
else:
    print("{} is not an even number".format(x))

# 範例輸入1

# 56
# 範例輸出1

# 56 is an even number.
# 範例輸入2

# 21
# 範例輸出2

# 21 is not an even number.