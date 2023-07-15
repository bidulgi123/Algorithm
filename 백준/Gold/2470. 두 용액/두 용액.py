import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int, input().split()))
b.sort()
left=0
right=a-1
q=10**15
while left < right:
    ans=b[left]+b[right]
    if abs(ans) < q :
        q=abs(ans)
        p=[b[left],b[right]]
    if ans == 0 :
        break
    if ans < 0 :
        left+=1
    else :
        right-=1
print(*p)