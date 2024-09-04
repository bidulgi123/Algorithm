import math
a, b, c = map(int, input().split())
ans = 0
for i in range(a, a + c):
    for j in range(b, b + i - a + 1):
        ans += math.comb(i - 1, j - 1)
print(ans)
