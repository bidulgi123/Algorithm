import sys
from collections import deque
input = sys.stdin.readline
a,b=map(int,input().split())
total=[]
x,y=0,0
for i in range(a):
    q=list(map(int,input().split()))
    total.append(q)
for i in range(a):
    for j in range(b):
        if total[i][j]==2:
            x,y=i,j
            break
visited=[[-1] * b for i in range(a)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j):
    visited[i][j]=1
    total[i][j]=0
    q=deque()
    q.append((i,j))
    while q :
        i, j = q.popleft()
        for p in range(4):
            nx=i+dx[p]
            ny=j+dy[p]
            if nx < 0 or nx >= a or ny < 0 or ny >= b :
                continue
            if total[nx][ny]==0:
                continue
            if visited[nx][ny] == -1 and total[nx][ny]==1:
                visited[nx][ny]= 1
                q.append((nx,ny))
                total[nx][ny]=total[i][j]+1
bfs(x,y)
for i in range(a):
    for j in range(b):
        if total[i][j]==1 and visited[i][j] == -1 :
            total[i][j] = -1
for i in total:
    print(*i)

