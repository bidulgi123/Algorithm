a = int(input())
b = list(map(int, input().split()))
total = []
for i in range(a):
    for j in range(a):
        if i != j:
            total.append((b[i] + b[j], i, j))
total.sort(key=lambda x: x[0])
ans = float('inf')
for i in range(len(total)):
    for j in range(i + 1, len(total)):
        if total[j][0] - total[i][0] >= ans:
            break
        if total[i][1] != total[j][1] and total[i][1] != total[j][2] and total[i][2] != total[j][1] and total[i][2] != total[j][2]:
            ans = min(ans, total[j][0] - total[i][0])
print(ans)
