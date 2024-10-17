import sys
import heapq
input = sys.stdin.readline

def dj(start):
    h = []
    visited = [float('inf')] * (n + 1)
    visited[start] = 0
    heapq.heappush(h, (0, start))
    while h :
        w, t = heapq.heappop(h)
        if visited[t] < w :
            continue
        for i in graph[t]:
            p = w + i[1]
            if p < visited[i[0]] :
                visited[i[0]]=p
                heapq.heappush(h,(p,i[0]))
    return visited

while True:
    n, m, s, c = map(int, input().split())
    if n == 0 and m == 0 and s == 0 and c == 0 :
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        t = list(map(int, input().split()))
        graph[t[0]].append((t[1], t[2]))
    print(dj(s)[c])

