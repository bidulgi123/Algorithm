a=int(input())
total = list(map(int, input().split()))
ans = [0] * a
for i in range(a):
    for j in range(i):
        if total[i]> total[j] and ans[i] < ans[j]:
            ans[i] = ans[j]
    ans[i] += 1
print(max(ans))