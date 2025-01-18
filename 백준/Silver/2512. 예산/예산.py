import sys
a = int(input())  
b = list(map(int, input().split()))  
c = int(input())
b.sort()
low, high = 0, max(b)  
result = 0
while low <= high:
    mid = (low + high) // 2 
    total = sum(min(mid, x) for x in b) 
    if total <= c:  
        result = mid  
        low = mid + 1 
    else:  
        high = mid - 1  
print(result)