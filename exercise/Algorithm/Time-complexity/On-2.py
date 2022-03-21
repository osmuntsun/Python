# O(10)
for i in range(10): 
    print(1)

# O(10^2)
for i in range(10):
    for j in range (10):
        print(1)

# O(10^2)
for i in range(10):
    for j in range (10):
        print(1)

#Time complexity = O(2n^2 + n)
#Time complexity = O(n^2) 取最大的次方那一項

#O(n^2) Selection Sort 選擇排序法
# n * (n+3) / 2 

Numbers = [41,33,17,80,61,5,55] # O(1)
length = len(Numbers) # O(1)

# O(7^2)
for i in range(length):
    min_index = i 
    for j in range(i+1,length):
        if Numbers[min_index] > Numbers[j]:
            min_index = j
    Numbers[min_index], Numbers[i] = Numbers[i], Numbers[min_index]

print(Numbers) # O(1)

# Time complexity = O(7^2)

# O(n^2) Insertion Sort 插入排序法
# n * (n+3) / 2 
Numbers = [41,33,17,80,61,5,55] # O(1)
​
length = len(Numbers) # O(1)
for i in range(1, length): # O(7^2)
    position = i
    value = Numbers[i]
    while position > 0 and Numbers[position-1] > Numbers[position]:
        Numbers[position], Numbers[position-1] = Numbers[position-1], Numbers[position]
        position -= 1
​
print(Numbers)

# Time complexity = O(n^2)