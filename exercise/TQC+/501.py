# TQC+ 程式語言Python 501 訊息顯示
# 設計說明：
# 請撰寫一程式，呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、學號（Student ID）和姓名（Name）並顯示這些訊息。

def DSN(DEP,stu,name):
   return print("\nDepartment:%s\nStudent ID:%s\nName:%s"%(DEP,stu,name))
x=input("DEP:")
y=input("stu:")
z=input("name:")
DSN(x,y,z)


# 輸入輸出：
# 輸入說明
# 三個字串
# 輸出說明
# 系別（Department）
# 學號（Student ID）
# 姓名（Name）
# 輸入輸出範例
# 範例輸入
# Information Management
# 123456789
# Tina Chen
# 範例輸出
# Department: Information Management
# Student ID: 123456789
# Name: Tina Chen