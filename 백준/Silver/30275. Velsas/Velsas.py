import sys
import math
input=sys.stdin.readline
a,b=map(int,input().split())
total=[int(input()) for i in range(a)]
start=0
end=1
cnt=math.inf
if len(total) == 1 :
    if sum(total) < b : 
        print('NEPAVYKS')
    else :
        print(1)
else:
    while start < a and end < a :
        high=sum(total[start:end+1])
        if high < b :
            end+=1
        else : 
            print(total[start:end+1])
            cnt=min(cnt,end-start+1)
            start+=1
    if cnt == math.inf:
        print('NEPAVYKS')
    else :
        print(cnt)