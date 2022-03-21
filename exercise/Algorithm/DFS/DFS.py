# DFS(Depth First Search) 深度優先搜尋

# Part I
print("--- Part I ---")
class Node:
    def __init__(self, s):
        self.data = s
        self.next = [None, None, None]


def build_tree():
    root = Node('red-1')
    root.next[0] = Node('orange-2')
    root.next[1] = Node('lime-3')
    root.next[2] = Node('green-4')
    root.next[0].next[0] = Node('yellow-5')
    root.next[2].next[0] = Node('blue-6')
    root.next[2].next[1] = Node('violet-7')

    return root


def dfs(start):
    if start is None:
        return
    print(start.data, ' 找過了.')
    for i in range(3):
        dfs(start.next[i])


tree = build_tree()
dfs(tree)

# Part II 
print("--- Part II ---")

inf = -1
e = []
visited = [False] * 7


def dfs(now):
    print(now, ' visited.')
    for j in range(1, 7):
        if not visited[j] and e[now][j] == 1:
            visited[j] = True
            dfs(j)


for i in range(0, 7):
    e.append([inf] * 7)  # e[i][j] 為 i 到 j 的距離, inf 代表走不到
for i in range(1, 7):
    e[i][i] = 0  # 0 代表就是自己

for i in range(0, 8):
    a, b = input().split()
    a, b = int(a), int(b)
    e[a][b] = 1  # 1 代表可以走到
    e[b][a] = 1

visited[1] = True
dfs(1)