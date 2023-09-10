from itertools import combinations
a,b=map(int,input().split())
for j in combinations([i for i in range(1,a+1)], b):
    print(*j)