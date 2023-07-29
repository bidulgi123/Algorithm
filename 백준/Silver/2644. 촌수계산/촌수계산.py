import sys
from collections import deque
input = sys.stdin.readline
a=int(input())
b,c=map(int,input().split())
total=[[] for i in range(a+1)]
visited=[-1] * (a+1)
for i in range(int(input())):
    d,e=map(int,input().split())
    total[d].append(e)
    total[e].append(d)
def bfs(n):    
    q=deque()
    q.append(n)
    visited[n]=0
    while q :
        m=q.popleft()
        for i in total[m]:
            if visited[i] == -1 :
                visited[i] = visited[m] + 1
                q.append(i)
bfs(b)
print(visited[c])

