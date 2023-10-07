import sys
import math
input=sys.stdin.readline
a=int(input())
b=list(map(int,input().split()))
b.sort()
ans=math.inf
ans_list = [-999,999,909]
for i in range(a-2):
    left=i+1
    right=a-1
    if sum(ans_list) == 0:
        break
    while left < right :
        q=b[i]+b[left]+b[right]
        if abs(ans) > abs(q):
            ans=abs(q)
            ans_list=[b[i],b[left],b[right]]
        if q < 0 :
            left+=1
        elif q > 0 :
            right-=1
        else : 
            break
print(*ans_list)       