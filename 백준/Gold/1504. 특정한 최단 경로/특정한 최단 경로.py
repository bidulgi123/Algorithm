import sys
import heapq
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
mid1, mid2 = map(int, input().split())
def dj(s):
    visited = [float('inf')] * (n + 1)
    h = []
    visited[s] = 0
    heapq.heappush(h, (0, s))
    while h :
        w, p = heapq.heappop(h)
        if visited[p] < w :
            continue
        for i in graph[p]:
            r = w + i[1]
            if r < visited[i[0]]:
                visited[i[0]] = r 
                heapq.heappush(h, (r, i[0]))
    return visited
mid_1 = dj(mid1)
mid_2 = dj(mid2)
ans = min(mid_2[1] + mid_2[mid1] + mid_1[n], mid_1[1] + mid_1[mid2] + mid_2[n],
          mid_2[1] + mid_2[mid1] + mid_1[mid2] + mid_2[n], mid_1[1] + mid_1[mid2] + mid_2[mid1] + mid_1[n])
if ans == float('inf'):
    print(-1)
else :
    print(ans)