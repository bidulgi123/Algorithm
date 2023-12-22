import heapq
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[list(map(int,input().split())) for i in range(a)]
s,x,y=map(int,input().split())
bi=[]
for i in range(a):
    for j in range(a):
        if total[i][j] != 0 :
            heapq.heappush(bi,(total[i][j],i,j))
move=[(0,1), (0,-1), (-1,0), (1,0)]
for i in range(s):
    mid_bi=[]
    while bi:
        start=heapq.heappop(bi)
        for j in move:
            dx=start[2]+j[0]
            dy=start[1]+j[1]
            if dx >= 0 and dy >= 0 and dx < a and dy < a :
                if total[dy][dx] == 0:
                    total[dy][dx]=start[0]
                    heapq.heappush(mid_bi,(start[0],dy,dx))
    bi=mid_bi
print(total[x-1][y-1])
