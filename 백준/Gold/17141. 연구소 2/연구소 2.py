import sys
from collections import deque 
from itertools import combinations
input = sys.stdin.readline
m, n = map(int, input().split())
bi_list = []
total= []
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(m):
    o = list(map(int, input().split()))
    total.append(o)
    for j in range(len(o)) :
        if o[j] == 2 :
            bi_list.append([_, j])

def bfs(v):
    q = deque(v)
    visited = [[-1 for _ in range(m)]  for i in range(m)]
    t = 0
    for s,f in q:
        visited[s][f] = 0

    while q:
        x,y = q.popleft()
        for i in move :
            dx = i[0] + x
            dy = i[1] + y
            if 0 <= dx < m and 0 <= dy < m:
                if visited[dx][dy] == -1 and total[dx][dy] != 1 :
                    q.append((dx,dy))
                    visited[dx][dy] = visited[x][y] + 1

    for i in range(m):
        for j in range(m):
            if total[i][j] != 1 and visited[i][j] == -1 :
                return float('inf')
            
    return max(sum(visited, []))

ans=float('inf')
for v in combinations(bi_list, n):
    ans = min(ans, bfs(v))
if ans==float('inf'):
    print(-1)
else :
    print(ans)    