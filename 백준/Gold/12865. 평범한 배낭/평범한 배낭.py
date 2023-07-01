import sys
from collections import deque
input=sys.stdin.readline
a,b=map(int, input().split())
mul=deque()
for i in range(a):
    c=list(map(int,input().split()))
    mul.append(c)
mul.appendleft([0,0])
total=[[0 for i in range(b+1)] for i in range(a+1)]
for i in range(1,a+1):
    for j in range(1, b+1):
        if j < mul[i][0] :
            total[i][j]=total[i-1][j]
        else : 
            total[i][j]=max(mul[i][1]+total[i-1][j-mul[i][0]],total[i-1][j])
print(total[a][b])