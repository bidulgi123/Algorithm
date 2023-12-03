import sys
input=sys.stdin.readline
a, b=map(int, input().split())
total=[input().rstrip() for i in range(a)]
total=sorted(sorted(total,reverse=True)[:9])
start=0
r=1
rank=[0]*10
cnt=0
for i in total:
    for j in i :
        cnt+=1
        if j != 'S' and j != '.':
            rank[int(j)]=r
            r+=1
            if cnt == start:
                rank[int(j)]-=1
                r-=1
            start=cnt
            cnt=0
            break
for i in range(1,len(rank)):
    print(rank[i])