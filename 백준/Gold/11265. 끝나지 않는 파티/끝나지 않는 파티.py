import sys
input = sys.stdin.readline
a, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(a)]
for k in range(a):
    for i in range(a):
        for j in range(a):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for _ in range(b):
    c, d, e = map(int, input().split())
    if graph[c - 1][d - 1] <= e :
        print('Enjoy other party')
    else :
        print('Stay here')