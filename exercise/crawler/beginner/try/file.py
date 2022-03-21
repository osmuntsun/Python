#儲存檔案
# filew=open('try/try.txt',mode="w",encoding="utf-8")#打開檔案
# filew.write("測試中文") #寫入
# filew.close() #關閉檔案

# with open('try/try.txt',mode='w',encoding="utf-8") as o:
#     o.write('測是可不可以阿!\nㄚㄚㄚㄚㄚㄚㄚㄚ')

#讀取檔案
# with open('try/try.txt',mode='r',encoding='utf-8') as o:
#     s=o.read() # .read()-讀取全部檔案
# print(s) #印出S

#讀取一行一行的檔案
# sum=0
# with open('try/try.txt',mode='r+',encoding='utf-8') as file:
#     for x in file: #一行一行的讀取
#         sum+=int(x) #讀出來的數字 轉換整數加總
# print(sum)

#用JSON格式讀取 複寫檔案
# import json
# with open("try/config.json",mode="r+",encoding="utf-8") as o:
#     all=json.load(o) #讀出
# print(all) #印出來all 是一個字典資料
# all['name']='osmuntsun'#修改變數中的資料
# #把最新的資料複寫回檔案中
# with open('try/config.json',mode='r+',encoding='utf-8') as o:
#     json.dump(all,o)#複寫回去

# print("osmuntsun=",all["name"])
