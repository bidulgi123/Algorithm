import sys
input=sys.stdin.readline
b,e = map(int, input().split())
c=[]
for i in range(b):
    c.append(int(input()))
total=[0]*(e+1)
total[0]=1
for i in c :
    for j in range(e+1):
        if j >= i :
            total[j] += total[j-i]
print(total[e])