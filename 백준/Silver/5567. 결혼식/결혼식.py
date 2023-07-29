from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
total=[[] for i in range(a+1)]
for i in range(b):
  c,d=map(int,input().split())
  total[c].append(d)
  total[d].append(c)
visited=[0]*(a+1)
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        a = q.popleft()
        for i in total[a]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[a] + 1
bfs(1)
cnt=0
for i in visited:
  if i > 1 and i < 4 :
    cnt+=1
print(cnt)