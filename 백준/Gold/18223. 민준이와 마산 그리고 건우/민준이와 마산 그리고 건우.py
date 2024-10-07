import heapq
import sys
input = sys.stdin.readline
v, e, p = map(int, input().split())
graph = [[] for i in range(v + 1) ]
for i in range(e):
    t = list(map(int, input().split()))
    graph[t[0]].append((t[1], t[2]))
    graph[t[1]].append((t[0], t[2]))

def dj(s):
    visited=[float('inf')]*(v + 1)
    h=[]
    visited[s]=0
    heapq.heappush(h,(0,s))
    while h :
        w,n=heapq.heappop(h)
        if visited[n] < w :
            continue
        for i in graph[n]:
            p=w+i[1]
            if p < visited[i[0]]:
                visited[i[0]]=p
                heapq.heappush(h,(p,i[0]))
    return visited

move = dj(1)
middle_move = dj(p)

if move[v] == middle_move[1] + middle_move[v] :
    print('SAVE HIM')
else :
    print('GOOD BYE')