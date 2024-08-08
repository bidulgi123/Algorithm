from collections import deque
import sys
input = sys.stdin.readline
a = int(input())
b = deque()
for i in range(a):
    c, d = input().split()
    b.append((c, int(d)))
while len(b) != 1 :
    start = b.popleft()
    for i in range(start[1] - 1):
        b.append(b.popleft())
    b.popleft()
print(b[0][0])