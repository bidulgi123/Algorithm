from bisect import bisect_left
a = int(input())
b = list(map(int, input().split()))
b.reverse()
total = [b[0]]

for i in range(1, a):
    if total[-1] < b[i] : 
        total.append(b[i])
    else :
        q = bisect_left(total, b[i])
        total[q] = b[i]

print(a - len(total))