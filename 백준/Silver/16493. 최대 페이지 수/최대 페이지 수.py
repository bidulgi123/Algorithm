import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[[0,0]]
for i in range(b):
    q=list(map(int, input().split()))
    total.append(q)
ans=[[0 for i in range(a+1)] for i in range(b+1)]
for i in range(1,b+1):
    for j in range(1,a+1):
        if j < total[i][0] :
            ans[i][j] = ans[i-1][j]
        else : 
            ans[i][j] = max(ans[i-1][j], total[i][1]+ans[i-1][j-total[i][0]])
print(ans[b][a])    