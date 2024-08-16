n = int(input()) 
t = list(map(int, input().split()))  
t.sort()
ans = 0  
i = 0
while i < n:
    start = t[i]
    ans += 1
    if i + 2 < n and t[i + 2] - start <= 10:
        i += 3  
    elif i + 1 < n and t[i + 1] - start <= 20:
        i += 2  
    else:
        i += 1 
print(ans)

