import sys
input = sys.stdin.readline
a = int(input())
total = [list(map(int, input().split())) for i in range(a)]
vis = [[0] * a for i in range(a)]
for first_s in range(a):
    for grade in range(5):
        for j in range(a):
            if total[first_s][grade] == total[j][grade]:
                vis[first_s][j] = 1
ans = [0] * a
for idx, q in enumerate(vis):
    ans[idx] = q.count(1)
mid = 0
name = 9999999999999999999999999
for i in range(a):
    if mid < ans[i]:
        mid = ans[i]
        name = i + 1
print(name)