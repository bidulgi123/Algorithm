import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[0]*(a+1)
for i in range(b):
    c,d,e=map(int,input().split())
    for j in range(c,d+1):
        total[j]=e
print(*total[1:])