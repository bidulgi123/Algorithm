from collections import deque
import sys
input=sys.stdin.readline
a=int(input())
b=deque(map(int, input().split()))
total=deque()
ans=[0] * a
total.append((b[0],0))
for i in range(1,a):
    while total:
        if total[-1][0] > b[i]:
            ans[i]=total[-1][1] + 1
            break
        else:
            total.pop()
    total.append((b[i],i))
print(*ans)