import sys
from collections import deque
from collections import Counter
input=sys.stdin.readline
while True:
    a=deque(map(str,input().split()))
    o=a.popleft()
    if o =='#' and len(a) == 0 :
        break
    t=''.join(a)
    t=t.lower()
    q=Counter(t)
    print(o,q[o])