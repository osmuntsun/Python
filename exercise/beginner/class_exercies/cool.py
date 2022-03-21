# ---------- main and name ---------- 
# def cool_func():
#     print('cool_func(): Super Cool!')


# if __name__ == '__main__':
#     print('Call it locally')
#     cool_func()

# __name__  =>  如果該檔案是被引用，其值會是模組名稱，
# 但若該檔案是(透過命令列)直接執行其值會是  =>  '__main__' <-字串


# ---------- Class教學 ----------
# class Car:
#     suppertedSrcs = ['console','file']
#     def read(src):
#         if src not in Car.suppertedSrcs:
#             print("not Supported")
#         else:
#             print('Read function',src)

# print(Car.suppertedSrcs)
# Car.read('HI')
# Car.read('console')

# ---------- Class實體物件 ----------

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

# #建立第一個實體物件
# p = Point(3,2)
# print(p.y+p.x)
# #建立第二個實體物件
# p2=Point(5,3)
# print(p2.x,p2.y)

#實例: FullName 實體物件的設計: 分開紀錄姓、名資料的全名
# class FullName:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
# name1 = FullName('C.W.','Peng')
# print(name1.first,name1.last)
# name2 = FullName('T.Y.','Lin')
# print(name2.first,name2.last)

# Point 實體物件的設計:平面座標上的點
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     # 定義實體方法
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5

# p = Point(3,4)
# p.show() # 呼叫實體方法 / 函式
# result=p.distance(0,0) #計算座標 3,4 和座標 0,0 之間的距離
# print(result)

# File 實體物件的設計:包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self,name):
        self.name = name
        self.file = None #尚未開啟檔案:初期是None
    # 實體方法
    def open(self):
        self.file=open(self.name,mode='r',encoding='utf-8')
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1 = File('data1.txt')
f1.open()
data = f1.read()
print(data)
#讀取第二個檔案
f2 = File('data2.txt')
f2.open()
data = f2.read()
print(data)