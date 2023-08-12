import sys
import heapq
import math
input=sys.stdin.readline
a,b=map(int,input().split())
total=[[] for i in range(a+1)]
visited=[math.inf]*(a+1)
h=[]
for i in range(b):
    o1,o2,o3=map(int,input().split())
    total[o1].append((o2,o3))
    total[o2].append((o1,o3))
def dj(s):
    visited[s]=0
    heapq.heappush(h,(0,s))
    while h :
        w,n=heapq.heappop(h)
        if visited[n] < w :
            continue
        for i in total[n]:
            p=w+i[1]
            if p < visited[i[0]]:
                visited[i[0]]=p
                heapq.heappush(h,(p,i[0]))

dj(1)
print(visited[a])
