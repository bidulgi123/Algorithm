from collections import deque
import sys
input = sys.stdin.readline
a=int(input())
c=deque()
for i in range(a):
    b=list(input().split())
    if b[0] == 'push':
        c.append(b[1])
    if b[0] == 'pop':
        try :
            print(c.popleft())
        except :
            print(-1)
    if b[0] == 'size':
        print(len(c))
    if b[0] == 'empty':
        if len(c) == 0:
            print(1)
        else :
            print(0)
    if b[0] == 'front':
        try:
            print(c[0])
        except :
            print(-1)
    if b[0] == 'back':
        try:
            print(c[-1])
        except :
            print(-1)