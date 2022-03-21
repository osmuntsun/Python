# TQC+ 程式語言Python 707 共同科目
# 設計說明：
# 請撰寫一程式，輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點（集合中不包含字串"end"）。
# 請依序分行顯示(1) X組和Y組的所有科目、(2)X組和Y組的共同科目、(3)Y組有但X組沒有的科目，以及(4) X組和Y組彼此沒有的科目（不包含相同科目）。
# 提示：科目須參考範例輸出樣本，依字母由小至大進行排序。

x_set=set()
y_set=set()
while True:
    x_input=input()
    if x_input=="end":
        break
    else:
        x_set.add(x_input)
while True:
    y_input=input()
    if y_input=="end":
        break
    else:
        y_set.add(y_input)
print(sorted(x_set.union(y_set)))
print(sorted(x_set.intersection(y_set)))
print(sorted(y_set.difference(x_set)))
print(sorted(x_set.symmetric_difference(y_set)))




# 輸入輸出：
# 輸入說明
# 輸入X組和Y組各自的科目至集合，直至end結束輸入
# 輸出說明
# X組和Y組的所有科目
# X組和Y組的共同科目
# Y組有但X組沒有的科目
# X組和Y組彼此沒有的科目（不包含相同科目）
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Enter group X's subjects:
# Math
# Literature
# English
# History
# Geography
# end
# Enter group Y's subjects:
# Math
# Literature
# Chinese
# Physical
# Chemistry
# end
# ['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Literature', 'Math', 'Physical']
# ['Literature', 'Math']
# ['Chemistry', 'Chinese', 'Physical']
# ['Chemistry', 'Chinese', 'English', 'Geography', 'History', 'Physical']