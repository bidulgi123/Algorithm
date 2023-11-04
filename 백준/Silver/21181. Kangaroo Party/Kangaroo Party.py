import sys
import math
input=sys.stdin.readline
a = int(input())
total=[int(input()) for i in range(a)]
ans=math.inf
for i in range(a-1):
    for j in range(i,a):
        mid=[]
        for q in range(a):
            mid.append(min((total[i]-total[q])**2, (total[j]-total[q])**2))
        ans=min(ans,sum(mid))
print(ans)