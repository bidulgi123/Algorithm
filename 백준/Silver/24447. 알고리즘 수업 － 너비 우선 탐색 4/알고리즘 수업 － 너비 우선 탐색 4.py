import sys
from collections import deque
input=sys.stdin.readline
a,b,c=map(int,input().split())
total=[[] for i in range(a+1)]
for i in range(b):
    q,u = map(int,input().split())
    total[q].append(u)
    total[u].append(q)
visited=[0] * (a+1)
node=[-1] * (a+1)
node[c]=0
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    node[x]=0
    cnt=1
    while q:
        m = q.popleft()
        total[m].sort()
        for i in total[m]:
            if visited[i] == 0:
                cnt+=1
                q.append(i)
                visited[i] = cnt
                node[i]=node[m]+1
bfs(c)
ans=0
for i in range(1,a+1):
    ans+=visited[i]*node[i]
print(ans)
