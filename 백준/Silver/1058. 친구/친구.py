import sys
input=sys.stdin.readline
a=int(input())
total=[list(input()) for i in range(a)]
ans=[[0]*a for i in range(a)]
for i in range(a):
    for j in range(a):
        for t in range(a):
            if j != t :
                if total[j][t] == 'Y' or (total[j][i] == 'Y' and total[i][t] == 'Y'):
                    ans[j][t]=1
answer=0
for i in ans :
    answer=max(answer, sum(i))
print(answer)