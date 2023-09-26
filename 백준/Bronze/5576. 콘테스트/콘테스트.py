import sys
input=sys.stdin.readline
a=[int(input()) for i in range(10)]
b=[int(input()) for i in range(10)]
a.sort(reverse=True)
b.sort(reverse=True)
print(sum(a[:3]),sum(b[:3]))