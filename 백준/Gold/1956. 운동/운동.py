import sys
input = sys.stdin.readline
v, e = map(int,input().split())
graph = [[float('inf')]*(v+1) for i in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
for k in range(1, v+1):
    for j in range(1, v+1):
        for t in range(1,v+1):
            graph[j][t] = min(graph[j][t], graph[j][k] + graph[k][t])
ans = float('inf')
for i in range(1,v+1):
    ans = min(ans, graph[i][i])
if ans == float('inf'):
    print(-1)
else :
    print(ans)