import sys
input = sys.stdin.readline
a, b = map(int, input().split())
t = [list(map(int, input().rstrip())) for _ in range(a)]
l = min(a, b)
ans = 1
for i in range(2, l + 1):
    for j in range(0, a - i + 1):
        for q in range(0, b - i + 1) :
            if t[j][q] == t[j + i - 1][q] == t[j][q + i - 1] == t[j + i - 1][q + i - 1] :
                ans = max(ans, i)
print(ans ** 2)