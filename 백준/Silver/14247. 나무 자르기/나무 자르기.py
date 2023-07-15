import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
c.sort()
ans=0
for i in range(a):
    ans+=b[i]+i*c[i]
print(ans)