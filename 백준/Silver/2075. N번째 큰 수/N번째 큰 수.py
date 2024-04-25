import heapq
import sys
input = sys.stdin.readline
a = int(input())
b = []  
for i in range(a):
    total = list(map(int, input().split()))
    for j in total:
        if len(b) < a:  
            heapq.heappush(b, j)
        elif b[0] < j: 
            heapq.heappop(b)
            heapq.heappush(b, j)  
print(heapq.heappop(b))