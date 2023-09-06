import sys
input=sys.stdin.readline
a=int(input())
total=[]
for i in range(a):
    b,c,d,e=map(str,input().split())
    c,d,e = map(int,(c,d,e))
    total.append((e,d,c,b))
total.sort()
print(total[-1][3])
print(total[0][3])
