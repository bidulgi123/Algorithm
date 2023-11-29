import sys
input=sys.stdin.readline
for i in range(int(input())):
    n=int(input())
    if n==0:
        tupC=(1,0)
    elif n==1 :
        tupC=(0,1)
    else :
        tupA=(1,0)
        tupB=(0,1)
    for i in range(n-1):
        tupC=tuple(sum(elem) for elem in zip(tupA, tupB))
        tupA=tupB
        tupB=tupC
    print(*tupC)