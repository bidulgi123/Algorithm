import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int,input().split()))
ans=0
q=b[0]
for i in range(1,a):
    if q < b[i] : 
        ans=max(b[i]-q,ans)
    else :
        q=b[i]
print(ans)