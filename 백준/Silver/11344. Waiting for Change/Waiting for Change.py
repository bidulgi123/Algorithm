from collections import deque 
from copy import deepcopy
import sys
input = sys.stdin.readline
for i in range(int(input())):
    input()
    cnt = 0
    total = deque()
    l = 0
    ans = ''
    for i in range(int(input())):
        b, c = input().split()
        c = int(c)
        if c == 20 :
            total.append(b)
        else :
            cnt += 1
        if total and cnt > 0 :
            cnt -= 1 
            total.popleft()
        if len(total) > l :
            ans = deepcopy(total)
            l = len(ans)
    if len(ans) != 0 :
        print(*ans)
    else :
        print('Line B stayed empty.')