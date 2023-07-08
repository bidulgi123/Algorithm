import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=list(map(int, input().split()))
total=[0,0]
q=0
for i in range(a):
    q+=c[i]
    total.append(q)
for i in range(b):
    e,f=map(int, input().split())
    print(total[f+1]-total[e])