import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[int(input()) for i in range(a)]
start, end = 1,max(total)
while (start<=end):
    c=(start+end)//2
    cnt=0
    for i in total:
        cnt+=i//c
    if cnt >= b :
        start = c+1
    else :
        end = c-1
print(end)