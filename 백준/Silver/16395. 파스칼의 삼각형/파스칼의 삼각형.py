n, k = map(int, input().split())
total = [[1 for _ in range(i)] for i in range(1, 31)]
for i in range(2, 30):
    for j in range(1, i):
        total[i][j] = total[i-1][j-1] + total[i-1][j]
print(total[n-1][k-1])