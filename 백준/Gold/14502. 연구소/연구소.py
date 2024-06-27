import sys 
from collections import deque
from itertools import combinations
import copy 

input = sys.stdin.readline
a, b = map(int, input().split())
graph = []
virus = []
space = []

for i in range(a):
    sec = list(map(int, input().split()))
    graph.append(sec)
    for j in range(b):
        if sec[j] == 2 :
            virus.append((i,j))
        if sec[j] == 0 :
            space.append((i,j))

move = [(0, 1),(1, 0),(-1, 0),(0, -1)]

def bfs(v, wall):
    q = deque(v)
    graph_b = copy.deepcopy(graph)
    
    for i, j in wall:
        graph_b[i][j] = 1
    
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < a and 0 <= ny < b and graph_b[nx][ny] == 0:
                graph_b[nx][ny] = 2
                q.append((nx, ny))

    cnt = sum(row.count(0) for row in graph_b)
    return cnt

ans = 0

for i in list(combinations(space, 3)):     
    ans = max(ans, bfs(virus, i))

print(ans)