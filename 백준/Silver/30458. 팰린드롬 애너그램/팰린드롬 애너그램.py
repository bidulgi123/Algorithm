import sys
from collections import Counter
input = sys.stdin.readline
a=int(input())
b=input().rstrip()
if b == b[::-1]:
    print('Yes')
else :
    if a % 2 == 0 :
        for key, value in Counter(b[:a//2]+b[a//2:]).items() :
            if value % 2 != 0 :
                print('No')
                sys.exit()
        print('Yes')
    else :
        for key, value in Counter(b[:a//2]+b[a//2+1:]).items() :
            if value % 2 != 0 :
                print('No')
                sys.exit()
        print('Yes')