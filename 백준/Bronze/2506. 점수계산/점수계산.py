import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int, input().split()))
ans=0
total=0
for i in range(a):
    if b[i] == 1 :
        ans+=1
        total+=ans
    else :
        ans=0
print(total)