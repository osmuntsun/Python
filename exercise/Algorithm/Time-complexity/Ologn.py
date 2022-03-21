# O(log n) Binary Search 二分搜尋法
# O(1)
Numbers = [5,17,33,41,55,61,80]
Find = 55 # O(1)
​
low = 0 # O(1)
high = len(Numbers) - 1 # O(1)
​
# O(log 7)
while low <= high: 
    mid = (low + high) // 2
    if Numbers[mid] > Find:
        high = mid - 1
    elif Numbers[mid] < Find:
        low = mid + 1
    else:
        break
​
print(mid)

# Time complexity = O(11)

