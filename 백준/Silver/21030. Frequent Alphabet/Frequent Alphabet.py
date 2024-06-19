from collections import defaultdict
N = int(input())
S = input()
T = input()
strr = 'abcdefghijklmnopqrstuvwxyz'
dp = [defaultdict(int) for _ in range(N + 1)]
for i in range(1, N + 1):
    for c in strr :
        dp[i][c] = dp[i-1][c]
        if S[i-1] == c:
            dp[i][c] = max(dp[i][c], dp[i-1][c] + 1)
        if T[i-1] == c:
            dp[i][c] = max(dp[i][c], dp[i-1][c] + 1)
ans = 0
for c in strr :
    ans = max(ans, dp[N][c])
print(ans)