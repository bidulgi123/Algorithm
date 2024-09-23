import sys
input = sys.stdin.readline
f = [1, 2]
while f[-1] < 10 ** 100 :
    f.append(f[-1]+f[-2])
while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break 
    cnt = 0 
    for i in f :
        if i >= a and i <= b :
            cnt += 1
        elif i > b :
            break
    print(cnt)
    