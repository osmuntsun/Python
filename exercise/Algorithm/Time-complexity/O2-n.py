# O(2^n) Fibonacci numbers 費波那契數列

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(10))

# Time complexity = O(2^10)
# 用遞迴太浪費時間 所以將 空間換取時間
# 可以讓時間複雜度變成 O(n)

table = [0]*3
table[0] = 0
table[1] = 1
​
for i in range(2,11):
    table[2] = table[1] + table[0]
    table[0] = table[1]
    table[1] = table[2]
​
print(table[2])