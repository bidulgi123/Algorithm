from collections import Counter
import sys
input = sys.stdin.readline
a, b =map(int, input().split())
t = [input().rstrip() for i in range(a)]
c_t = [word for word in t if len(word) >= b]
counter_t = Counter(c_t)
for i in sorted(counter_t.keys(), key=lambda x: (-counter_t[x], -len(x), x)):
    print(i)