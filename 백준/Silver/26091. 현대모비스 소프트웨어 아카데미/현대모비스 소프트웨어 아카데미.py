import sys
import math
input=sys.stdin.readline
a,b=map(int,input().split())
total=list(map(int,input().split()))
total.sort()
start=0
end=a-1
ans=0
while start < end : 
    if total[start]+total[end] < b : 
        start +=1
    else :
        start +=1
        end-=1
        ans+=1
print(ans)
