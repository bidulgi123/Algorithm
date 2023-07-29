import sys
from bisect import bisect_left, bisect_right
a=int(input())
b=list(map(int, input().split()))
total=[b[0]]
for i in b:
    if total[-1] < i:
        total.append(i)
    else : 
        p=bisect_left(total, i)
        total[p]=i
print(len(total))