import sys
input = sys.stdin.readline
total={}
total[0]=0
total[1]=1
a, b = 1, 1
for i in range(2,100001):
    total[b] = i
    a, b = b, a + b
for i in range(int(input())):
    c = int(input())
    print(total[c])