import sys
input=sys.stdin.readline
a=int(input())
ans = count = 0
times = []
for _ in range(a):
  st, en = map(int, input().split())
  times.append([st, 1])
  times.append([en, -1])
times.sort()
for _, val in times:
  count += val
  ans = max(ans, count)
print(ans)