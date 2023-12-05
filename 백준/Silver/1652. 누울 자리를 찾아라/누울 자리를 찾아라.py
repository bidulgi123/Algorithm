import sys
input=sys.stdin.readline
a=int(input())
total=[input().rstrip() for i in range(a)]
b = [''.join(x) for x in zip(*total)]
garo=0
sero=0
for i, j in zip(total, b):
    mid_garo=0
    mid_sero=0
    for q, t in zip(i,j) :
        if q =='.':
            mid_garo+=1
        else :
            if mid_garo >= 2 :
                garo+=1
                mid_garo=0
            else :
                mid_garo=0
        if t =='.':
            mid_sero+=1
        else :
            if mid_sero >= 2 :
                sero+=1
                mid_sero=0
            else :
                mid_sero=0
    if mid_sero >= 2 :
        sero+=1
    if mid_garo >= 2 :
        garo+=1
print(garo, sero)