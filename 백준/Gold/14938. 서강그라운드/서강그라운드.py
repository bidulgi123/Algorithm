import sys
import heapq
input = sys.stdin.readline
n, m, r = map(int,input().split())
item = list(map(int, input().split()))
graph=[[] for i in range(n + 1)]
for _ in range(r):
    a, b, c = map(int ,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    visited = [float('inf')] * (n + 1)
    visited[start]=0
    q=[]
    heapq.heappush(q, (0, start))
    while q :
        dis, now = heapq.heappop(q)
        if visited[now] < dis :
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < visited[i[0]] :
                visited[i[0]] = cost 
                heapq.heappush(q, (cost, i[0]))
    return visited
ans = 0
for i in range(1, n+1):
    li = dijkstra(i)
    middle = 0
    for idx, j in enumerate(li) :
        if j <= m :
            middle+=item[idx-1]
    ans = max(middle, ans)
print(ans)