import sys
input = sys.stdin.readline
a = int(input())
INF = float('inf')
graph = [[INF] * (a + 1) for _ in range(a + 1)]
line = []

def check(a, b):
    if a[0] <= b[1] and a[1] >= b[0]:
        return True
    return False

for _ in range(a):
    s, e = map(int, input().split())
    line.append((s, e))

for i in range(a):
    for j in range(i, a):
        if check(line[i], line[j]):
            graph[i+1][j+1], graph[j+1][i+1] = 1, 1  

for k in range(1, a + 1):
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    z, y = map(int, input().split())
    if graph[z][y] == INF:
        print(-1)
    else:
        print(graph[z][y])