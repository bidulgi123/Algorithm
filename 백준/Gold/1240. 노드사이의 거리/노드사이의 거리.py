import sys
import math
sys.setrecursionlimit(100000000)
input = sys.stdin.readline
m, n = map(int, input().split())
graph = [[] for i in range(m+1)]
for j in range(m-1):
    c, d, e = map(int, input().split())
    graph[c].append((d,e))
    graph[d].append((c,e))

def dfs(start, s, no):
    global ans
    if start == no:
        print(s)
        return True
    visit[start] = 1
    for i in graph[start]:
        if visit[i[0]] != 1:
            if dfs(i[0], s + i[1], no):
                return True
    return False

for _ in range(n):
    ans=0
    visit = [0] * (m + 1)
    q, t = map(int, input().split())
    dfs(q,0,t)