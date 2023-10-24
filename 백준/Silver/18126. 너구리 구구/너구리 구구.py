import sys
sys.setrecursionlimit(12312341)
input=sys.stdin.readline
a=int(input())
total=[[] for i in range(a+1)]
visited=[0]*(a+1)
distance=[0]*(a+1)
for i in range(a-1):
    b,c,d=map(int,input().split())
    total[b].append([c,d])
    total[c].append([b,d])
def dfs(j):
    visited[j] = 1
    for q, w in total[j]:
        if visited[q] != 1:
            distance[q] = w + distance[j]
            dfs(q)
    return
dfs(1)
print(max(distance))