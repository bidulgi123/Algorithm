a, b = map(int, input().split())
total = list(map(int, input().split()))
start, end = 1, max(total)
while start <= end : 
    mid = (start + end) // 2 
    ans = 0
    for i in total :
        if i > mid : 
            ans += i - mid
    if ans >= b : 
        start = mid + 1
    else :
        end = mid - 1   
print(end)