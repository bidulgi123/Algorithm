import sys
import heapq
import math
input=sys.stdin.readline
a=int(input())
for i in range(1,a+1):
    b,c=map(int, input().split())
    total=list(map(int, input().split()))
    start=0
    end=b-1
    cnt=0
    while start < end : 
        if total[start] + total[end] < c :
            start +=1 
        elif total[start] + total[end] > c : 
            end -=1
        else :
            cnt+=1
            start +=1
            end -=1 
    print(f"Case #{i}: {cnt}")