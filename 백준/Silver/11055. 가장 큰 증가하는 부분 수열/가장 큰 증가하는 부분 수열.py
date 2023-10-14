import sys
input=sys.stdin.readline
a=int(input())
total = list(map(int, input().split()))
ans = total.copy()
for i in range(a):
    for j in range(i):
        if total[i]>total[j] :
            ans[i] = max(ans[i],ans[j]+total[i])
print(max(ans))