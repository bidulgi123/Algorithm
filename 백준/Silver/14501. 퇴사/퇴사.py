import sys
input=sys.stdin.readline
a=int(input())
total=[list(map(int,input().split())) for i in range(a)]
ans=[0]*(a+1)
for i in range(len(total)-1,-1,-1):
    if i + total[i][0] > a:
        ans[i] = ans[i+1]
    else:
        ans[i] = max(total[i][1] + ans[i+total[i][0]], ans[i+1])
print(ans[0])