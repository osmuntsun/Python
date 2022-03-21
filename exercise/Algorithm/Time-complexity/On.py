x = 10 # O(1)
for i in range(x): # O(10)
    print("HI")

# Time complexity = O(11)

# O(n) Easy Search 簡易搜尋
# O(1)
Pokemons = ["卡丘","胖丁","尼龜","比獸",
"呆獸","種子","小剛"]
for Pokemon in Pokemons: # O(7)
  if Pokemon == "呆獸":
    print("找到呆獸！")
    break
  else:
    print("這個櫃子裡不是呆獸")

#Time complexity = WorstCase O(8)