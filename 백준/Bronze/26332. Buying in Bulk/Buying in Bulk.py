import sys
input=sys.stdin.readline
a=int(input())
for i in range(a):
    b,c=map(int,(input().split()))
    print(b,c)
    print(b*c-(b-1)*2)
