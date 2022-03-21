# TQC+ 程式語言Python 405 不定數迴圈-分數等級
# 設計說明：
# 請撰寫一程式，以不定數迴圈的方式輸入一個正整數（代表分數），之後根據以下分數與GPA的對照表，印出其所對應的GPA。
# 假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：

while True:
    x=eval(input("輸入分數："))
    
    if x>=90 and x<=100:
        print("分數為：%d\nGPA：A"%x)
    elif x>=80 and x<=89:
        print("分數為：%d\nGPA：B"%x)
    elif x>=70 and x<=79:
        print("分數為：%d\nGPA：C"%x)
    elif x>=60 and x<=69:
        print("分數為：%d\nGPA：D"%x)
    elif x>=0 and x<=59:
        print("分數為：%d\nGPA：E"%x)
    elif x==-9999:
        break
        
# 分　數	GPA
# 90 ~ 100	A
# 80 ~ 89	B
# 70 ~ 79	C
# 60 ~ 69	D
# 0 ~ 59	E
# 輸入輸出：
# 輸入說明
# 一個正整數，直至-9999結束輸入
# 輸出說明
# 依輸入值，輸出對應的GPA
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# 75
# C
# 39
# E
# 100
# A
# 85
# B
# 65
# D
# -9999