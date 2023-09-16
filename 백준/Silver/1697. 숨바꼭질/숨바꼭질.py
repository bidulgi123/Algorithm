import sys
from collections import deque 
input=sys.stdin.readline
a,b=map(int,input().split())
visit=[0] * (100001) 
total=deque()
total.append(a)
while total:
    now=total.popleft()
    if now == b :
        break
    else :
        move=[now-1,now+1,now*2]
        for i in move :
            if i >= 0 and i <= 100000 and visit[i] == 0 :
                visit[i] = visit[now]+1
                total.append(i)
print(visit[b])
