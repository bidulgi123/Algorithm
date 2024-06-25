import sys 
input = sys.stdin.readline
l = int(input())
total = list(map(int, input().split()))
cnt = [0] * 1001
ans = 0
for i in total : 
    cnt[i] += 1
for j in range(len(cnt)) :
    ans += min(2, cnt[j])
print(ans)