import sys
input=sys.stdin.readline
for j in range(int(input())):
    a=int(input())
    dp=[1] * max(4,(a+1))
    dp[2] = 2
    dp[3] = 4
    for i in range(3,a+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[a])