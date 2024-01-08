import sys
input=sys.stdin.readline
total=[list(map(int, input().split())) for i in range(11)]
total.sort()
a=0
b=0
for i in total:
    a+=b+i[0]
    b+=i[0]
    a+=20*i[1]
print(a)