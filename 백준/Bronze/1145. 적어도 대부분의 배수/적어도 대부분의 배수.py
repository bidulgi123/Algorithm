import math
from itertools import combinations
a=list(map(int, input().split()))
a=list(combinations(a,3))
t=[]
for i in a :
    t.append(math.lcm(i[0],i[1],i[2]))
print(min(t))