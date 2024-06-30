import sys
from collections import deque
input = sys.stdin.readline
a, b =map(int ,input().split())
t = list(map(int, input().split()))
q = deque()
for i in range(a):
    now = t[i]
    while q and q[-1][0] > now :
        q.pop()
    q.append((now, i))
    if q[0][1] + b <= i :
        q.popleft()
    print(q[0][0], end=' ')