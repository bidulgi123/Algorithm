import sys
from collections import deque
input = sys.stdin.readline
b = deque()
ans = []
for i in range(int(input())):
    t = input().split()
    if t[0] == 'push':
        b.append(t[-1])
    elif t[0] == 'pop':
        ans.append(b.popleft() if b else -1)
    elif t[0] == 'size':
        ans.append(str(len(b)))
    elif t[0] == 'empty':
        ans.append(0 if b else 1)
    elif t[0] == 'back':
        ans.append(b[-1] if b else -1)
    elif t[0] == 'front':
        ans.append(b[0] if b else -1)
for i in ans :
    print(i)        