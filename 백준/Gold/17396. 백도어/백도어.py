import heapq
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
sight = list(map(int, input().split()))
graph = [[] for i in range(n)]

for _ in range(m):
    t = list(map(int, input().split()))
    graph[t[0]].append((t[1], t[2]))
    graph[t[1]].append((t[0], t[2]))

def dj(start):
    h = []
    visited = [float('inf')] * n
    visited[start] = 0
    heapq.heappush(h, (start, 0))
    while h :
        p = heapq.heappop(h)
        if p[1] > visited[p[0]] or sight[p[0]] == 1 :
            continue
        for i in graph[p[0]]:
            q=p[1]+i[1]
            if q < visited[i[0]] and sight[p[0]] != 1:
                visited[i[0]]=q
                heapq.heappush(h,(i[0],q))
    return visited
v = dj(0)
if v[-1] != float('inf'):
    print(v[-1])
else :
    print(-1)   