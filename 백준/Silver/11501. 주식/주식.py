import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a = int(input())
    total = list(map(int, input().split()))
    ans = 0 
    mid = 0 
    for i in range(a-1, -1, -1):
        if total[i] > mid:
            mid = total[i]
        else: 
            ans += mid - total[i]
    print(ans)