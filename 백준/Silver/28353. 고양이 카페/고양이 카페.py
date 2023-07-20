import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=list(map(int, input().split()))
total.sort()
left=0
right=a-1
cnt=0
while left < right:
    q=total[left]+total[right]
    if q > b :
        right-=1
    elif q <= b :
        left+=1
        right-=1
        cnt+=1
print(cnt)