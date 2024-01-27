from bisect import bisect_left
a,b=map(int,input().split())
total=[]
for i in range(a):
    c,d,e = map(int,input().split())
    for i in range(e):
        total.append(c+d*i)
total.sort()
try:
    print(total[bisect_left(total,b)]-b)
except:
    print(-1)