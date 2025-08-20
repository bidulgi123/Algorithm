import sys
input = sys.stdin.readline
a, b = map(int, input().split())
total = []
for i in range(a):
    c, d = map(int, input().split())
    if c - d < 0 : 
        total.append(abs(c-d))
    else :
        b -= 1
total.sort()
if b > 0 :
    print(total[b - 1])
else :
    print(0)