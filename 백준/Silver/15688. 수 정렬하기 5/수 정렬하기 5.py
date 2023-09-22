import sys
input=sys.stdin.readline
total=[int(input()) for i in range(int(input()))]
total.sort()
for i in total:
    print(i)