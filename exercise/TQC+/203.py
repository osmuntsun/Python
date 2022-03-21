# 203_閏年判斷

# 題目說明:

# 請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏

x=eval(input("輸入西元年："))

if x%4==0 and x%100!=0:
    print("{} is a leap year".format(x))
elif x%100==0 and x%400!=0:
    print("{} is not a leap year".format(x))
elif x%400==0:
    print("{} is a leap year".format(x))
else:
    print("{} is not a leap year".format(x))

# 範例輸入1

# 1992
# 範例輸出1

# 1992 is a leap year.
# 範例輸入2

# 2010
# 範例輸出2

# 2010 is not a leap year.