import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total={}
for i in range(a):
    c,d=map(str,input().rstrip().split())
    total[c]=d
for j in range(b):
    c=input().rstrip()
    print(total[c])