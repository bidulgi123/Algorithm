import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[int(input()) for i in range(a)]
total.sort()
start=0
end=a-1
cnt=0
while start<end:
    if total[start]+total[end] <= b:
        cnt+= end-start
    else :
        start-=1
        end-=1
    start+=1
print(cnt)