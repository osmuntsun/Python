#定義類別、與類別屬性(封裝在類別中的變數和函式)
#定義一個類別 Text, 有兩個屬性 dic 和 os
class Text:
    dic=['sin','file']
    def os(src):
        if src not in Text.dic:
            print("no err")
        else:
            print(Text.dic,src)
#使用類別
print(Text.dic)
Text.os('file')
Text.os('hi')
