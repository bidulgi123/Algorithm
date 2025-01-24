import sys
input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a - 1][b - 1] = t
k = int(input())
g = list(map(int, input().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j :
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = []
load = INF
for i in range(n):
    dis = max([graph[i][j - 1] + graph[j - 1][i] for j in g])
    if dis < load :
        ans = []
        ans.append(i + 1)
        load = dis
    elif dis == load :
        ans.append(i + 1)

print(*ans)