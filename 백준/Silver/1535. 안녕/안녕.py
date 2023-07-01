from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
b=deque(map(int, input().split()))
c=deque(map(int, input().split()))
b.appendleft(0)
c.appendleft(0)
total=[[0 for i in range(100)] for i in range(a+1)]
for i in range(1,a+1):
    for j in range(1,100):
        if j < b[i] :
            total[i][j] = total[i-1][j]
        else : 
            total[i][j] = max(c[i]+total[i-1][j-b[i]], total[i-1][j])
print(total[a][99])