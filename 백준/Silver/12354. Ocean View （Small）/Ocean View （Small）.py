import sys
from collections import deque
input = sys.stdin.readline
a=int(input())
for i in range(1,a+1):
    input()
    b=deque(map(int,input().split()))
    cnt=0
    if len(b) == 1 :
        print(f"Case #{i}: {cnt}")
    else :
        for j in range(len(b)-1):
            if b[j+1] <= b[j]:
                cnt+=1
        print(f"Case #{i}: {cnt}")