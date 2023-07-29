import sys
from collections import deque
import math
input=sys.stdin.readline
a=int(input())
b=int(input())
total=[[math.inf]*(a+1) for i in range(a+1)]
for i in range(b):
 c,d,e=map(int,input().split())
 if total[c][d] > e :
    total[c][d] = e
for k in range(1,a+1):
    total[k][k]=0
    for i in range(1,a+1):
        for j in range(1,a+1):
            total[i][j] = min(total[i][j], total[i][k] + total[k][j])
for i in range(1,len(total)):
   total[i] = deque(total[i])
   total[i].popleft()
   for j in range(a):
    if total[i][j] == math.inf :
        total[i][j] = 0
        print(total[i][j], end=" ")
    else :
        print(total[i][j], end=" ")
   print()
