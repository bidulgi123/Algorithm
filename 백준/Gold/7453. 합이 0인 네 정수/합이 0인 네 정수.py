import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a, b, c, d = [], [], [], []

for _ in range(n):
    a1, b1, c1, d1 = map(int, sys.stdin.readline().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)

AB_sum = defaultdict(int)
for x in a:
    for y in b:
        AB_sum[x + y] += 1

count = 0
for x in c:
    for y in d:
        target = -(x + y)
        if target in AB_sum:
            count += AB_sum[target]

print(count)
