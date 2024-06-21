import sys
input = sys.stdin.readline
a, b = map(int, input().split())
total = []
prefix_sum = [[0] * (a + 1) for _ in range(a + 1)]
for _ in range(a):
    row = list(map(int, input().split()))
    total.append(row)
for i in range(1, a + 1):
    for j in range(1, a + 1):
        prefix_sum[i][j] = (prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1] + total[i - 1][j - 1])
for _ in range(b):
    t = list(map(int, input().split()))
    x1, y1, x2, y2 = t
    result = (prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])
    print(result)