# TQC+ 程式語言Python 708 詞典合併
# 設計說明：
# 請撰寫一程式，自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。

# x_set_input=set()
# y_set_input=set()
# x_dic_input={}
# y_dic_input={}
# while True:
#     x_digital=input("1")
#     if x_digital=="end":
#         break
#     else:
#         x_set_input.add(x_digital)
# while True:
#     y_digital=input("2")
#     if y_digital=="end":
#         break
#     else:
#         y_set_input.add(y_digital)
# x_set_input=sorted(x_set_input,reverse=False)
# y_set_input=sorted(y_set_input,reverse=False)

x_dic_input={}
while True:
    x_key_digital=input("KEY:")
    if x_key_digital=='end':
        break
    x_valse_digital=input("valse:")
    x_dic_input[x_key_digital]=x_valse_digital
x_dic_input=sorted(x_dic_input,reverse=False)




# 輸入輸出：
# 輸入說明
# 輸入兩個詞典，直至end結束輸入
# 輸出說明
# 合併兩詞典，並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值
# 輸入輸出範例
# 輸入與輸出會交雜如下，輸出的部份以粗體字表示
# Create dict1:
# Key: a
# Value: apple
# Key: b
# Value: banana
# Key: d
# Value: durian
# Key: end
# Create dict2:
# Key: c
# Value: cat
# Key: e
# Value: elephant
# Key: end
# a: apple
# b: banana
# c: cat
# d: durian
# e: elephant