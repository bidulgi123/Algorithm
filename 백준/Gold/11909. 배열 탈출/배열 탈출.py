import sys
input = sys.stdin.readline

a = int(input())
graph = [list(map(int, input().split())) for _ in range(a)]

dp = [[float('inf')] * a for _ in range(a)]
dp[0][0] = 0

for i in range(a):
    for j in range(a):
        if i > 0:
            require = max(0, graph[i][j] - graph[i-1][j] + 1)
            dp[i][j] = min(dp[i][j], dp[i-1][j] + require)
        if j > 0:
            require = max(0, graph[i][j] - graph[i][j-1] + 1)
            dp[i][j] = min(dp[i][j], dp[i][j-1] + require)

print(dp[a-1][a-1])
