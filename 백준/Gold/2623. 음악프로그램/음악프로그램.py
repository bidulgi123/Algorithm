import sys
from collections import deque
v, e = map(int, input().split())
ind = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
for _ in range(e):
    t = list(map(int, input().split()))
    for i in range(1, t[0]):
        graph[t[i]].append(t[i + 1])
        ind[t[i + 1]] += 1

def topology_sort():
    result=[]
    q = deque()
    for i in range(1, v + 1):
        if ind[i] == 0:
            q.append(i)
    while q:
        n=q.popleft()
        result.append(n)
        for i in graph[n]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)
    return result
ans = topology_sort()
if len(ans) != v : 
    print(0)
else:
    for i in ans:
        print(i)