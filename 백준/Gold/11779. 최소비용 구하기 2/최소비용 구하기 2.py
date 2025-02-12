import heapq
import sys
input = sys.stdin.readline

def dj(s):
    visited[s] = 0
    heap = []
    heapq.heappush(heap, (0, s)) 

    while heap:
        w, n = heapq.heappop(heap)
        if visited[n] < w:
            continue
        for weight, next_node in total[n]:
            p = w + weight
            if p < visited[next_node]:
                visited[next_node] = p
                prev[next_node] = n  
                heapq.heappush(heap, (p, next_node))

def get_path(end):
    path = []
    while end != -1:
        path.append(end)
        end = prev[end]
    return path[::-1]  

INF = float('inf')
a = int(input()) 
b = int(input())  
total = [[] for _ in range(a + 1)]
visited = [INF] * (a + 1)
prev = [-1] * (a + 1)  

for _ in range(b):
    start, end, weight = map(int, input().split())
    total[start].append((weight, end))  

s, e = map(int, input().split())
dj(s)
path = get_path(e)
print(visited[e])
print(len(path))
print(*path)