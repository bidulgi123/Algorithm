import sys
input=sys.stdin.readline
y,x,inven=map(int,input().split())
total=[list(map(int, input().split())) for i in range(y)]
block=0
time=10000000000000
start=min(map(min,total))
end=max(map(max,total))+1
for i in range(start,end):
    up=0
    down=0
    for j in range(y):
        for t in range(x):
            if total[j][t] > i :
                down += total[j][t] - i
            else :
                up += i - total[j][t]
    if down + inven >= up :
        w=up+(down * 2)
        if time >=  w :
            time = w
            block = i
print(time, block)