# TQC+ 程式語言Python 607 成績計算
# 設計說明：
# 請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
# 提示：平均分數輸出到小數點後第二位。

sum_total=0
sum_all=[]
average_total=0
average_all=[]
for i in range(3):
    for j in range(5):
        digital_input=eval(input("第%d個學生第%d次成績:"%((i+1),(j+1))))
        sum_total+=digital_input
    average_total=float(sum_total/5)
    average_all.append(average_total)
    average_total=0
    sum_all.append(sum_total)
    sum_total=0
    print()
for x in range(3):
    print("第%d個學生\nSum:%d\nAverage:%.2f"%((x+1),sum_all[x],average_all[x]))

# 輸入輸出：
# 輸入說明
# 三位學生各五筆成績
# 輸出說明
# 格式化輸出每位學生的總分及平均分數
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# The 1st student:
# 78
# 89
# 88
# 70
# 60
# The 2nd student:
# 90
# 78
# 66
# 68
# 78
# The 3rd student:
# 69
# 97
# 70
# 89
# 90
# Student 1
# #Sum 385
# #Average 77.00
# Student 2
# #Sum 380
# #Average 76.00
# Student 3
# #Sum 415
# #Average 83.00