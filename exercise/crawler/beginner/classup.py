# class IO:
#     def __init__(self):
#         self.x=3
#         self.y=4
# #建立實體物件
# #此實體物件包含x和Y兩個實體屬性
# a=IO()
#--------------------------------------
# class IO:
#     def __init__(self,x,y):
#         self.name1=x
#         self.name2=y
# #建立實體物件
# #建立時,可直接傳入參數資料
# a=IO(1,5)
# a1=IO(10,5)
# #建立實體物件,並取得實體屬性資料
# #實體物件.實體物件名稱
# print(a.name1,a.name2)
# print(a1.name1,a1.name2)
#---------------------------------------
#FULLNAME(全名) 實體物件的式記:分開記錄姓,名資料的全名
# class FullName:
#     def __init__(self,x,y):
#         self.first=x #first是實體物件名稱
#         self.last=y #first是實體物件名稱
# name1=FullName("os","my")
# print(name1.first,name1.last)

#point 實體物件的設計: 平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
# p=Point(3,4)
# p.show()#呼叫實體方法/函式
# re=p.distance(0,0) #計算座標3,4和座標0,0之間的距離
# print(re)

#file 實體物件的設計:包裝檔案讀取的程式
# class File:
#     #初始化函式
#     def __init__(self,name):
#         self.name=name
#         self.file=None #尚未開啟檔案:初期是None
#     # 實體方法
#     def open(self):
#         self.file=open(self.name,mode="r+",encoding="utf-8")
#     # 讀出檔案資料
#     def read(self):
#         return self.file.read()
# #讀取第一個檔案
# p=File("data1.txt")
# p.open() #打開
# end=p.read() #讀取
# print(end) #印出
# #讀取第二個檔案
# p2=File("data2.txt")
# p2.open()
# end=p2.read()
# print(end)