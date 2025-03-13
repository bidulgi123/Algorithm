import sys
from bisect import bisect_left
input = sys.stdin.readline 
a, b = map(int, input().split())
title = {}
values = []

for _ in range(a):
    name, value = map(str, input().split())
    value = int(value)
    if not value in title :
        title[value] = name
        values.append(value)

values.sort()

for _ in range(b):
    you = int(input())
    print(title[values[bisect_left(values, you)]])