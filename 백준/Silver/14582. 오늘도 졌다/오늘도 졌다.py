a=list(map(int, input().split()))
b=list(map(int, input().split()))
team_a=0
team_b=0
flag=0
for i in range(len(a)):
    team_a += a[i]
    if team_a > team_b :
        flag=1
    team_b += b[i]
if flag==1 and team_b > team_a :
    print('Yes')
else :
    print('No')