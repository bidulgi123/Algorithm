import sys
input=sys.stdin.readline
for i in range(int(input())):
    b=list(input())
    c = len(b)//2 
    if b[c-1] == b[c]:
        print('Do-it')
    else: 
        print('Do-it-Not')