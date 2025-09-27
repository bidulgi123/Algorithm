import sys
input = sys.stdin.readline
a, b = map(int, input().split())
num = int(input())
hz = [int(input()) for _ in range(num)]
total = [abs(b - hz[q]) + 1 for q in range(num)]
total.append(abs(a-b))
print(min(total))
