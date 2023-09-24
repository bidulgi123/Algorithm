import sys
from collections import deque
input=sys.stdin.readline
a,b=map(int,input().split())
total=[]
for i in range(b):
    total.append(list(map(int,input().split())))
dq=deque()
for i in range(a):
    for j in range(b):
        if total[j][i]==1:
            dq.append((j,i))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= b or ny < 0 or ny >= a:
            continue
        if total[nx][ny] == -1:
            continue
        if total[nx][ny] == 0:
            total[nx][ny] = total[x][y] + 1
            dq.append((nx, ny))
flag=0
for i in total :
    if 0 in set(i):
        flag=1
if flag==0:
    print(max(map(max,total))-1)
else : 
    print(-1)