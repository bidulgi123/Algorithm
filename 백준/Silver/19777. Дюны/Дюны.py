import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())
min_num, max_num = math.inf, 0
total=[]
for i in range(a):
    c, d, e = map(int, input().split())
    if c < min_num : 
        min_num=c
    if d > max_num:
        max_num=d
    total.append([c,d,e])
for j in range(b):
    q=int(input())
    p=0
    for li in total:
        if q >= li[0] and q <= li[1]:
            if li[0] % 2 == q % 2 :
                p+=li[2]
            else :
                p-=li[2]
        else :
            continue
    print(p)