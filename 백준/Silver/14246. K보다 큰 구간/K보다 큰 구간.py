a = int(input())
t = list(map(int, input().split()))
b = int(input())
prefix_sum = [0] * (a + 1)
for i in range(1, a + 1):
    prefix_sum[i] = prefix_sum[i - 1] + t[i - 1]
cnt = 0
start, end = 0, 1
while start < a:
    while end <= a and (prefix_sum[end] - prefix_sum[start] <= b):
        end += 1
    if end <= a:
        cnt += a - end + 1
    start += 1
print(cnt)