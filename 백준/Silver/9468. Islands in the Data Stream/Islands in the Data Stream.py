import sys
from collections import deque
input=sys.stdin.readline
for i in range(int(input())):
  a=deque(map(int,input().split()))
  num=a.popleft()
  iter_list=set(a)
  iter_list.remove(0)
  cnt=0
  plag=0
  for i in iter_list:
    for j in a :
      if j == i :
        plag=1
      if j < i and plag==1 :
        cnt+=1
        plag=0
  print(num,cnt)
