s=""
for i in range(1,10):
    for a in range(1,10):
        if i%2==1:
            if a%2==1:
                s=s+"＊"
            else:
                s=s+"　"
        else:
            if a%2==0:
                s=s+"＊"
            else:
                s=s+"　"
    s=s+"\n"
print(s)

with open("A.txt",mode="r+",encoding="utf-8") as fox:
    fox.write(s)