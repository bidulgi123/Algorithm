import sys
input=sys.stdin.readline
for i in range(int(input())):
    input()
    a,b=map(int,input().split())
    total=[list(input().rstrip()) for i in range(a)]
    total_t=[list(j) for j in zip(*total)]
    cnt=0
    for i in total:
        cnt += "".join(i).count(">o<")
    for i in total_t:
        cnt += "".join(i).count("vo^")
    print(cnt)