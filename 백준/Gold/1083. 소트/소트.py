a = int(input())
b = list(map(int, input().split()))
c = int(input())
for i in range(a):
    leng = b.index(max(b[i:(min(a, c + i + 1))]))
    for j in range(leng, i, -1):
        if b[j - 1] < b[j] :
            b[j - 1], b[j] = b[j], b[j - 1]
            c -= 1
    if c <= 0 :
        break
print(*b)