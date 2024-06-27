s = 0
t = 0
for i in range(1, 6):
    q = list(map(int, input().split()))
    if s < sum(q) :
        t = i
        s = sum(q)
print(t, s)