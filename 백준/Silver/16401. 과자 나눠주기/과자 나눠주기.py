from bisect import bisect_left, bisect_right
from collections import deque
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=deque(map(int, input().split()))
first=1
end=1000000000
ans=0
while True:
  if first>end:
    break
  else :
    check=(first+end)//2
    cnt=0
    for i in total:
      cnt+=i//check
    if cnt>=a:
      ans = check
      first = check+1
    else :
      end = check-1
print(ans)
