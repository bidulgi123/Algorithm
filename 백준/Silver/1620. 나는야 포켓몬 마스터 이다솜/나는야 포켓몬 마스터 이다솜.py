import sys
input=sys.stdin.readline
total={}
a, b = map(int, input().split())
for i in range(1,a+1):
    c=input().rstrip()
    total[c]=i
    total[str(i)]=c
for j in range(b):
    d=input().rstrip()
    print(total[d])