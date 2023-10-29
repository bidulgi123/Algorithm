import sys
input=sys.stdin.readline
for i in range(3):
    total=sum([int(input()) for i in range(int(input()))])
    if total < 0 :
        print('-')
    elif total > 0 :
        print('+')
    else :
        print(0)