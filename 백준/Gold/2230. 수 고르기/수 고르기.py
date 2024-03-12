import sys
import math
input=sys.stdin.readline
a,b=map(int,input().split())
total=[int(input()) for i in range(a)]
total.sort()
start=0
end=0
m=math.inf
while end < a :
    mi = total[end]-total[start]
    if mi < b :
        end+=1
    elif mi > b :
        start+=1
        m=min(mi,m)
    else :
        m=b
        break
print(m)