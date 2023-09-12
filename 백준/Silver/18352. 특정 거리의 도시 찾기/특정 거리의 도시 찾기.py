import sys
import heapq
import math
input=sys.stdin.readline
a,b,c,d=map(int,input().split())
total=[[] for i in range(a+1)]
for i in range(b):
    o,p=map(int,input().split())
    total[o].append((p,1))
visited=[math.inf]*(a+1)
h=[]
def djik(s):
    visited[s]=0
    heapq.heappush(h,(0,s))
    while h:
        w,n=heapq.heappop(h)
        if visited[n] < w :
            continue
        for i in total[n]:
            p=w+i[1]
            if p < visited[i[0]]:
                visited[i[0]]=p
                heapq.heappush(h,(p,i[0]))
djik(d)
flag=0
for i in range(len(visited)):
    if visited[i] == c:
        print(i)
        flag=1
if flag!=1:
    print(-1)