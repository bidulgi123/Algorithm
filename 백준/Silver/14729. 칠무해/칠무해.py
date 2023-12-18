import sys
input=sys.stdin.readline
total=[float(input().rstrip()) for i in range(int(input()))]
total.sort()
for i in range(7):
    print("{:.3f}".format(total[i]))