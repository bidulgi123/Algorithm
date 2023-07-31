import sys
input=sys.stdin.readline
while True:
    a=input().rstrip()
    if a == 'END':
        break
    print(a[::-1])
