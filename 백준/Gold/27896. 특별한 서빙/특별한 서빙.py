import sys
import heapq
input = sys.stdin.readline
h = []
a, b = map(int, input().split())
t = list(map(int, input().split()))
c = 0
ans = 0
for i in t :
    heapq.heappush(h, -i)
    c += i 
    if c >= b : 
        q = heapq.heappop(h)
        c -= -q * 2 
        ans += 1
print(ans)