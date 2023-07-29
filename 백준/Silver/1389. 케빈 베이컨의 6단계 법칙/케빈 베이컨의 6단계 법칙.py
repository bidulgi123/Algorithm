import sys
from collections import deque
import math
input=sys.stdin.readline
a,b=map(int, input().split())
total=[[math.inf]*(a+1) for i in range(a+1)]
for i in range(b):
 c,d=map(int,input().split())
 total[c][d] = 1
 total[d][c] = 1
for k in range(1,a+1):
    total[k][k] = 0
    for i in range(1,a+1):
        for j in range(1,a+1):
            total[i][j] = min(total[i][j], total[i][k] + total[k][j])
ans=math.inf
q=0
for i in range(1,len(total)):
   total[i] = deque(total[i])
   total[i].popleft()
   if ans > sum(total[i]):
      ans = sum(total[i])
      q=i
print(q)