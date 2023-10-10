import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
a, b = map(int, input().split())
total = [list(map(int, input().split())) for i in range(a)]
visited = [[-1] * b for i in range(a)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(y, x):
    if y == (a - 1) and x == (b - 1):
        return 1
    if visited[y][x] != -1:
        return visited[y][x]
    visited[y][x] = 0
    for q, i in move:
        nx, ny = x + q, y + i
        if 0 <= nx < b and 0 <= ny < a and total[ny][nx] < total[y][x]:
            visited[y][x] += dfs(ny, nx)
    return visited[y][x]
print(dfs(0, 0))