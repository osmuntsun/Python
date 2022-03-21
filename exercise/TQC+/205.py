# 205_字元判斷

# 題目說明:

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。
# 例如：a為英文字母、9為數字、$為其它字元

x=str(input("輸入字元:"))

# 變數.isalpha()判斷是否為英文字母
# 變數.isdigit()判斷是否為數字
if x.isalpha():
    print('{} is an alphabet.'.format(x))
elif x.isdigit():
    print('{} is an number.'.format(x))
else:
    print('{} is a symbol.'.format(x))

# 範例輸入1

# P
# 範例輸出1

# P is an alphabet.
# 範例輸入2

# @
# 範例輸出2

# @ is a symbol.
# 範例輸入3

# 7
# 範例輸出3

# 7 is a number.