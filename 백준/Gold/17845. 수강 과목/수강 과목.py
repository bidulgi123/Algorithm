import sys
input=sys.stdin.readline
a,b=map(int,input().split())
study=[[0,0]]
for i in range(b):
    q=list(map(int, input().split()))
    study.append(q)
total=[[0 for i in range(a+1)] for i in range(b+1)]
for i in range(1,b+1):
    for j in range(1,a+1):
        if j < study[i][1] :
            total[i][j] = total[i-1][j]
        else :
            total[i][j] = max(total[i-1][j], study[i][0]+total[i-1][j-study[i][1]])
print(total[b][a])