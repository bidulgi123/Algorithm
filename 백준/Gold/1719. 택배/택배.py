import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
INF = float('inf')

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

def dijkstra(start):
    visited = [INF] * (n + 1)
    visited[start] = 0
    node = [['-'] for _ in range(n + 1)]  
    q = []
    heapq.heappush(q, (0, start, []))  
    while q:
        dis, now, move = heapq.heappop(q)
        if visited[now] < dis:
            continue
        for next_node, weight in graph[now]:
            cost = dis + weight
            if cost < visited[next_node]:
                visited[next_node] = cost
                node[next_node] = move + [next_node]  
                heapq.heappush(q, (cost, next_node, node[next_node]))
    for i in node[1:]:
        print(i[0], end=' ')
    print()
    return visited

for z in range(1, n + 1):
    dijkstra(z)
