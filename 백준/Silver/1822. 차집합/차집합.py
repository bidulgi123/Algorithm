import sys
input=sys.stdin.readline
a,b=map(int,input().split())
c=set(map(int, input().split()))
d=set(map(int, input().split()))
print(len(c-d))
print(*sorted(list(c-d)))