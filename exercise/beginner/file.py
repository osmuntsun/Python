# #儲存檔案
# file=open("int.txt",mode="w",encoding="utf-8")#開起
# file.write("Hello\nfile\n你在幹嘛?")#操作檔案
# file.close()#關閉檔案
with open("int.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")

#讀出檔案
# with open("int.txt",mode="r",encoding="utf-8") as file:
#     date=file.read()
# print(date)

#讀出文件中的數字然後加總
# sum=0
# with open("int.txt",mode="r",encoding="utf-8") as file:
#     for s in file:
#         sum+=int(s)   
# print(sum)

#使用json格式讀取
import json
with open("config.json",mode="r") as file:
    date=json.load(file) #json讀取進來是一個字典資料[]
print(date)
date["name"]="BANG" #修改變數中的資料
#把最新的資料復寫回檔案中
with open("config.json",mode="w") as file:
    date=json.dump(date,file)#寫回檔案中
# print("name: ",date["name"])
# print("version: ",date["version"])