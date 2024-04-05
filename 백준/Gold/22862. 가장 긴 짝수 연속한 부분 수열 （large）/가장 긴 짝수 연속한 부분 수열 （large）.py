n, k = map(int, input().split())
total = list(map(int, input().split()))
start, end = 0, 0
cnt, ans = 0, 0
while start < n:
    if cnt > k:
        if total[end] %2 == 1 :
            cnt -=1
        end +=1
        continue
    else:
        if total[start] %2 == 1 :
            cnt +=1
        start +=1
    ans = max(ans, start - end - cnt)
print(ans)