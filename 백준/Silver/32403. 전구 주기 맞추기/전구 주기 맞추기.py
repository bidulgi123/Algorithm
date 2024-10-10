import math
from bisect import bisect_left
a, b = map(int, input().split())
t = list(map(int, input().split()))

def find_divisor(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)          
            divisors.add(n // i)     
    divisors.add(0)
    divisors.add(math.inf)
    return sorted(divisors)

q = find_divisor(b)
cnt = 0
for i in t :
    idx = bisect_left(q, i)
    cnt += min(abs(i - q[idx]), abs(i - q[idx - 1]))
print(cnt)