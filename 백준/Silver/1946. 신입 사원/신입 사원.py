from collections import deque
import sys
input=sys.stdin.readline
for i in range(int(input())):
    a=int(input())
    total=deque()
    cnt=1
    for i in range(a):
        b=list(map(int, input().split()))
        total.append(b)
    total=sorted(total)
    m=total[0][1]
    for i in range(1,a):
        if m > total[i][1]:
            m = total[i][1]
            cnt+=1
    print(cnt)
            