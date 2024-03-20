import sys
input = sys.stdin.readline
a = int(input())
b = list(map(int, input().split()))
di = [1 for i in range(a+1)]
dir = [1 for i in range(a+1)]
for i in range(a):
    for j in range(i):
        if b[i] > b[j]:
            di[i] = max(di[i], di[j]+1)
for i in range(a-1,-1,-1):
    for j in range(i-1,-1,-1):
        if b[i] < b[j]:
            dir[j] = max(dir[j], dir[i]+1)
bi = 0
for i, j in zip(di, dir):
    bi = max(bi, i+j-1)
print(bi)