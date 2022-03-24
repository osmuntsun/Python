# from urllib.parse import quote

# data_name = '汽座'
# data = quote(data_name,'12')
# print(data)


IP_list = []
with open("./ip_data.csv",mode="r", encoding="utf-8-sig") as f:
    for data in f:
        data = data.replace('\n','')
        IP_list.append(data)
    del IP_list[0]

print(IP_list)