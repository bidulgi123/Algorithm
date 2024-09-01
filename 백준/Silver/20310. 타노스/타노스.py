a = list(input())
b = a.count('0')//2
c = a.count('1')//2
for _ in range(b):
    del a[-a[::-1].index('0')-1]
for _ in range(c):
     del a[a.index('1')]
print(*a, sep='')