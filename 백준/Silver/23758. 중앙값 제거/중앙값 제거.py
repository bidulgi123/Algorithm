a = int(input())
b = list(map(int,input().split()))
b.sort()
if a % 2 == 0 :
    mid = a // 2
else :
    mid = a // 2 + 1
ans = 0
for i in range(mid):
    c = b[i]
    while c > 1 :
        c //= 2 
        ans += 1 
print(ans + 1)