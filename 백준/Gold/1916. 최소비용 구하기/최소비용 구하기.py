import sys
import heapq
import math
input=sys.stdin.readline
a=int(input())
b=int(input())
total=[[] for i in range(a+1)]
for i in range(b):
    q,w,e=map(int,input().split())
    total[q].append((w,e))
start,end=map(int,input().split())
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
djik(start)
print(visited[end])