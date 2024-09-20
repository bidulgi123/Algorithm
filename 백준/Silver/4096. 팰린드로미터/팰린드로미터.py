import sys
input = sys.stdin.readline
while True :
    a = input().rstrip()
    if a == '0' :
        break
    l = len(a)
    t = int(a)
    while True :
        st = '0'*(l - len(str(t)))+str(t)
        if st == st[::-1]:
            print(t - int(a))
            break
        t += 1
