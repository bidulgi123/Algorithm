import sys
input = sys.stdin.readline
n, k, e = map(int, input().split())
t = []
algo = [0 for _ in range(31)]
for _ in range(n):
    m, d = map(int, input().split())
    mid = set(map(int, input().split()))
    t.append((d, mid))

t.sort(key=lambda x: x[0])

start = 0
end = 0
ans = 0

while start < n:
    while end < n and t[end][0] - t[start][0] <= e:
        for i in t[end][1]:
            algo[i] += 1
        end += 1

    union = 0
    inter = 0
    for i in algo:
        if i >= 1:
            union += 1
        if i == end - start:
            inter += 1

    ans = max(ans, (union - inter) * (end - start))

    for i in t[start][1]:
        algo[i] -= 1
    start += 1

print(ans)