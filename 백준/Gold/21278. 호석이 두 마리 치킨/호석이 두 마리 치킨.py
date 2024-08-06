import sys
input = sys.stdin.readline
a, b = map(int, input().split())
total = [[float('inf')]*(a+1) for i in range(a+1)]
for i in range(b):
    c, d = map(int, input().split())
    total[c][d] = 1
    total[d][c] = 1 
for k in range(1,a+1):
    total[k][k]=0
    for i in range(1,a+1):
        for j in range(1,a+1):
            total[i][j] = min(total[i][j], total[i][k] + total[k][j])
ans = []
s = float('inf')
for i in range(1, a + 1):
    for j in range(1, a + 1): 
        mid = 0
        for k in range(1, a + 1):
            mid += min(total[i][k], total[j][k]) * 2
        if s > mid :
            s = mid
            ans = [i, j, s]
print(*ans)