import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
total=list(map(int,input().split()))
total.sort()
left=0
right=a-1
ans=0
while left < right :
    pp=total[left]+total[right]
    if pp == b :
        left+=1
        right-=1
        ans+=1
    elif pp > b :
        right-=1
    else :
        left+=1
print(ans)