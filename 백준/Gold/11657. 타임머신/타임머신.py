import sys
import math
input = sys.stdin.readline
n, m = map(int,input().split())
total = [list(map(int,input().split())) for _ in range(m)]
dist = [math.inf] * (n + 1)
def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            st = total[j][0]
            end = total[j][1]
            w = total[j][2]
            if dist[st] != math.inf and dist[end] > dist[st] + w : 
                dist[end] =  dist[st] + w 
                if i == n - 1 :
                    return True
    return False 
cycle = bf(1)
if cycle :
    print(-1)
else :
    for i in range(2, n+1):
        if dist[i] == math.inf:
            print(-1)
        else :
            print(dist[i])