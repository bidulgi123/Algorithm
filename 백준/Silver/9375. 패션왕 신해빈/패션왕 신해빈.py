import sys
input=sys.stdin.readline
a=int(input())
for i in range(a):
    b=int(input())
    total={}
    for t in range(b):
        c, d = map(str, input().split())
        if d not in total:
            total[d] = 1
        else:
            total[d] += 1 
    ans=1
    for j in total:
        ans *= total[j] + 1
    print(ans-1)