n, k = map(int, input().split())
mak = [int(input()) for _ in range(n)]
mak.sort()

def bisect():
    left = 1
    right = mak[-1]
    result = 0 

    while left <= right:
        mid = (left + right) // 2
        ans = sum(now // mid for now in mak)  
        if ans >= k:  
            result = mid  
            left = mid + 1
        else:  
            right = mid - 1 

    return result

print(bisect())