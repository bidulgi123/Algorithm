import sys
input = sys.stdin.readline
a = int(input())
for __ in range(1, a+1):
    x, y, t = map(int, input().split())
    matrix = [[0] * y for _ in range(x)]
    prefix_sum = [[0] * (y+1) for _ in range(x+1)]
    for _ in range(t):
        j, k = map(int, input().split())
        matrix[j][k] = 1
    for i in range(x):
        for j in range(y):
            prefix_sum[i+1][j+1] = matrix[i][j] + prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]
    cnt = 0
    for i in range(1, x+1):
        for j in range(1, y+1):
            max_size = min(x - i + 1, y - j + 1)
            for size in range(1, max_size + 1):
                total_sum = (prefix_sum[i+size-1][j+size-1]
                                - prefix_sum[i+size-1][j-1]
                                - prefix_sum[i-1][j+size-1]
                                + prefix_sum[i-1][j-1])
                if total_sum == 0:
                    cnt += 1
                else:
                    break
    print(f"Case #{__}: {cnt}")