import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
mul = deque()
for i in range(a):
    c = list(map(int, input().split()))
    mul.append(c)
mul.appendleft([0, 0])
total = [0] * (b + 1)
for i in range(1, a + 1):
    new_total = [0] * (b + 1)
    for j in range(1, b + 1):
        if j < mul[i][0]:
            new_total[j] = total[j]
        else:
            new_total[j] = max(mul[i][1] + total[j - mul[i][0]], total[j])
    total = new_total
print(total[b])