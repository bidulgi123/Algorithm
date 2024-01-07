import sys
input=sys.stdin.readline
for i in range(int(input())):
    print(len(set([input().rstrip() for i in range(int(input()))])))