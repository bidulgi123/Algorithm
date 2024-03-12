from collections import deque
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
ind = [0] * (a+1)
ans = [1] * (a+1)
graph = [[] for _ in range(a+1)]
for _ in range(b):
    c, d = map(int,input().split())
    graph[c].append(d)
    ind[d] += 1
def sorting():
    q = deque()
    for i in range(1,a+1):
        if ind[i]==0:
            q.append(i)
    while q:
        n=q.popleft()
        for i in graph[n]:
            ind[i] -= 1
            ans[i] = ans[n] + 1
            if ind[i] == 0:
                q.append(i)
    return ans
q=sorting()
print(*q[1:])