import sys
input = sys.stdin.readline
input()
a=set(list(map(int, input().split())))
b=set(list(map(int, input().split())))
print(len(a-b)+len(b-a))
