import sys
input=sys.stdin.readline
n,s=map(int, input().split())
nums=[int(input()) for i in range(n)]
start, end=0, 0
current_sum=0
min_length=sys.maxsize
while True:
    if current_sum >= s:
        min_length=min(min_length, end - start)
        current_sum-=nums[start]
        start+=1
    elif end == n:
        break
    else:
        current_sum+=nums[end]
        end+=1
if min_length == sys.maxsize:
    print("NEPAVYKS")
else:
    print(min_length)