import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[int(input()) for i in range(a)]
start=0
end=a-1
cnt=0
while start < end :
    if total[start]+total[end] < b :
        start +=1
    elif total[start]+total[end] > b :
        end-=1
    else :
        start+=1
        end-=1
        cnt+=1
print(cnt)