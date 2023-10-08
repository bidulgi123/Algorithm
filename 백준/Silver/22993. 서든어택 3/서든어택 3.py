import sys
from collections import deque
input=sys.stdin.readline
a=int(input())
b=deque(map(int,input().split()))
start=b.popleft()
b=sorted(b)
for i in b :
    if start > i : 
        start += i
    else : 
        print('No')
        sys.exit()
print('Yes')


