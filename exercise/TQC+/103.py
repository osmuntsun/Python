# 請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、
# 欄與欄間隔一個空白字元、每列印兩個的方式，
# 先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。 

# 範例輸入1

# I
# enjoy
# learning
# Python
# 範例輸出1

# |         I      enjoy|
# |  learning     Python|
# |I          enjoy     |
# |learning   Python    |

# 但注意如果是字串的話，默認預設是向左靠齊，不同於數值型態是靠右對齊


a=input()
b=input()
c=input()
d=input()

print("│{:>10s} {:>10s}│".format(a,b)) #字串是加 s 數字加 d
print("│{:>10s} {:>10s}│".format(c,d))
print("│{:10s} {:10s}│".format(a,b))
print("│{:10s} {:10s}│".format(c,d))
