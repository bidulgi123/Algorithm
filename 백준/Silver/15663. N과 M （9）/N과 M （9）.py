import sys
from itertools import permutations
input=sys.stdin.readline
a,b=map(int,input().split())
total=list(map(int, input().split()))
for i in sorted(list(set(list(permutations(total,b))))):
    print(*i)