n = int(input())
a = 0
l= len(str(n))
for i in range(1, l):
    a += i * 9 * (10 ** (i - 1))
a += l * (n - 10 ** (l - 1) + 1)
print(a)
