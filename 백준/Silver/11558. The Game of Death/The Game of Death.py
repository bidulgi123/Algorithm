import sys
input=sys.stdin.readline
a=int(input())
for i in range(a):
    b=int(input())
    total=[0]
    for i in range(b):
        total.append(int(input()))
    visited=[0]*len(total)
    cnt=0
    start=1
    while True:
        cnt+=1
        if visited[start]==1 and total[start]!=b:
            print(0)
            break
        if total[start]==b:
            print(cnt)
            break
        visited[start]=1
        start=total[start]
    