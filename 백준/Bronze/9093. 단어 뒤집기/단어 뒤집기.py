import sys
input=sys.stdin.readline
a=int(input())
for i in range(a):
    b=list(input().split())
    print(*list(map(lambda x: x[::-1],b)))