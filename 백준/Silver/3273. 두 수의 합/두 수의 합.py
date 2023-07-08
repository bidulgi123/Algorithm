import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int, input().split()))
c=int(input())
left=0
right=a-1
b.sort()
cnt=0
while left < right :
    if b[left] + b[right] > c :
        right-=1
    elif b[left] + b[right] < c :
        left +=1
    else :
        cnt+=1
        right-=1
        left+=1
print(cnt)