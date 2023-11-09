import sys
from itertools import combinations
input=sys.stdin.readline
for i in range(int(input())):
    total=[input().rstrip() for j in range(int(input()))]
    total = list(combinations(total, 2))
    for i in total:
        first=i[0]+i[1]
        end=i[1]+i[0]
        if first == first[::-1]:
            print(first)
            break
        if end == end[::-1]:
            print(end)
            break
    else:
        print(0)