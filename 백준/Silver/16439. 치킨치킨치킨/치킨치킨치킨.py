from itertools import combinations
import sys
input=sys.stdin.readline
a, b = map(int,input().split())
total = [list(map(int,input().split())) for _ in range(a)]
ans=0
for i in combinations(range(b), 3):
    t=0
    for j in range(a):
        t+=max(total[j][i[0]],total[j][i[1]],total[j][i[2]])
    ans=max(ans,t)
print(ans)