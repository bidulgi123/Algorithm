from collections import deque 
import sys
import copy
input=sys.stdin.readline
a=int(input())
b=deque(map(int, input().split()))
c=int(input())
d=deque(map(int, input().split()))
b=deque(sorted(b,reverse=True))
d=deque(sorted(d,reverse=True))
cnt=0
if b[0] < d[0] :
    print(-1)
else :
    while len(d) != 0 :
        c=copy.deepcopy(b)
        d=deque(sorted(d,reverse=True))
        for i in range(len(d)):
            if len(c) == 0 or len(d) == 0  :
                break
            if c[0] >= d[0] :
                d.popleft()
                c.popleft()
            else : 
                d.append(d.popleft())
        cnt+=1
    print(cnt)