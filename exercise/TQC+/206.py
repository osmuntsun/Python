# 206_等級判斷

 

# 題目說明:

# 請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：

#  分　數   等級
# 80 ~ 100   A
# 70 ~ 79    B
# 60 ~ 69    C
#  <= 59     F

x=eval(input("輸入分數："))

if x>=80 and x<=100:
    print("A")
elif x>=70 and x<=79:
    print("B")
elif x>=60 and x<=69:
    print("C")
elif x<=59 and x>=0:
    print("F") 
else:
    print("不在1-100的範圍內")


# 範例輸入1

# 79
# 範例輸出1

# B