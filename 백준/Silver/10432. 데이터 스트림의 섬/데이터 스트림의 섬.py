import sys
from collections import deque
input=sys.stdin.readline
a=int(input())
for _ in range(a):
    b=deque(map(int,input().split()))
    num=b.popleft()
    start=[]
    cnt=0
    for i in b :
        while len(start) !=0 :
            if start[-1] > i :
                start.pop()
                cnt += 1
            else :
                break
        if len(start) ==0 or start[-1] < i:
            start.append(i)
    print(num, cnt)