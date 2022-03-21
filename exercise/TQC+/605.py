# TQC+ 程式語言Python 605 成績計算
# 設計說明：
# 請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。
# 提示：平均值輸出到小數點後第二位。

total_digital=0
total_list=[]
for i in range(10):
    digital_input=eval(input("輸入第%d個:"%(i+1)))
    total_list.append(digital_input)
big_data=max(total_list)
small_data=min(total_list)
for j in range(len(total_list)):
    if big_data==small_data:
        print("最小值與最大值相同")
        break
    elif big_data!=total_list[j] and small_data!=total_list[j]:
        total_digital+=total_list[j]
print("%d\n%.2f"%(total_digital,total_digital/8))


# 輸入輸出：
# 輸入說明
# 十個數字
# 輸出說明
# 總和
# 平均
# 輸入輸出範例
# 範例輸入
# 89
# 78
# 67
# 80
# 75
# 98
# 77
# 89
# 76
# 60
# 範例輸出
# 631
# 78.88