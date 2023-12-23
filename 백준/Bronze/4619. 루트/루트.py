import sys
input=sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a==0 and b == 0:
        break
    i = 0
    while i**b < a:
        i += 1
    if i**b-a < a-(i-1)**b :
        print(i)
    elif i**b-a > a-(i-1)**b :
        print(i-1)