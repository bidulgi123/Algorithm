import sys
input=sys.stdin.readline
for i in range(int(input())):
    b=int(input())
    c=list(map(int, input().split()))
    e=int(input())
    total=[0]*(e+1)
    total[0]=1
    for i in c :
        for j in range(e+1):
            if j >= i :
                total[j] += total[j-i]
    print(total[e])