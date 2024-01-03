import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=list(map(int,input().split()))
start=0
end=1
cnt=0
while start<=end:
    if end > a:
        break
    if b > sum(total[start:end]):
        end+=1
    elif b < sum(total[start:end]):
        start+=1
    else :
        cnt+=1
        end+=1
print(cnt)