import sys
from itertools import permutations
def calculate_mid_value(q, b):
    while len(q) > 1:
        q = [q[i-1] + q[i] for i in range(1, len(q))]
    return q[0] == b
a, b = map(int, input().split())
total = [i for i in range(1, a+1)]
total_list = permutations(total, a)
for i in total_list:
    if calculate_mid_value(i, b):
        print(*i)
        sys.exit()