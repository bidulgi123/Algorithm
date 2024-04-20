n = int(input())
u = [0] * (n + 1)
for i in range(2, n + 1):
    if i % 2 == 0:
        u[i] = (u[i-1] * 2 + 1) % 1000000007
    else:
        u[i] = (u[i-1] * 2 - 1) % 1000000007
print(u[n])