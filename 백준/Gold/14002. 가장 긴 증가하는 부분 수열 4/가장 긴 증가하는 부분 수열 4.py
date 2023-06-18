from collections import deque
a=int(input())
total = list(map(int, input().split()))
ans = [0] * a
for i in range(a):
    for j in range(i):
        if total[i]> total[j] and ans[i] < ans[j]:
            ans[i] = ans[j]
    ans[i] += 1
p=max(ans)
so=deque()
print(p)
for j in range(len(ans)-1,-1,-1):
    if ans[j] == p :
        so.appendleft(total[j])
        p-=1
print(*so)