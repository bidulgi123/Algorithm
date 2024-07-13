import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
prefix_sum = [0] * (a + 1)
for i in range(1,a+1):
    prefix_sum[i] = prefix_sum[i - 1] + b[i - 1]
for i in range(int(input())):
    c, d = map(int, input().split())
    print(prefix_sum[d]-prefix_sum[c - 1])