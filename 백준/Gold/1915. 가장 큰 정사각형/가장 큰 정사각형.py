import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[list(map(int,list(input().rstrip()))) for i in range(a)]
dp=[[0]*b for i in range(a)]
ans=0
for i in range(a):
  for j in range(b):
    if i == 0 or j == 0 :
      dp[i][j] = total[i][j]
    elif total[i][j] == 0 :
      dp[i][j] = 0 
    else :
      dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    ans=max(dp[i][j],ans)
print(ans*ans)