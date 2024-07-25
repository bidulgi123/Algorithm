import sys 
from bisect import bisect_left
input = sys.stdin.readline
for i in range(int(input())):
    input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    cnt = 0
    for i in a :
        cnt += bisect_left(b, i)
    print(cnt)