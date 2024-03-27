import sys
input = sys.stdin.readline
a, b = map(int, input().split())
total = list(map(int, input().split()))
prefix_sum = [0]
for num in total:
    prefix_sum.append(prefix_sum[-1] + num)
start, end = 0, 1
ans = float('inf')
while end <= a:
    mid = prefix_sum[end] - prefix_sum[start]
    if mid >= b:
        ans = min(ans, end - start)
        start += 1
    else:
        end += 1
if ans == float('inf'):
    print(0)
else:
    print(ans)