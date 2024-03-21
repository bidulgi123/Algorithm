import sys
import heapq
import math
input = sys.stdin.readline
n, v, e = map(int,input().split())
kist, food = map(int,input().split())
team = list(map(int,input().split()))
graph=[[] for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijstra(start):
    dis = [math.inf] * (v+1)
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist :
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return dis

ans = 0

for i in team:
    team_member = dijstra(i)
    if team_member[kist] == math.inf:
        ans -=1
    if team_member[food] == math.inf:
        ans -=1
    if team_member[food] != math.inf:
        ans += team_member[food]
    if team_member[kist] != math.inf:
        ans += team_member[kist]

print(ans)