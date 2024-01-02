import sys
input=sys.stdin.readline
for i in range(int(input())):
    r=int(input())
    total=[int(input()) for i in range(r)]
    for j in range(1,10**6):
        p=set()
        for q in total:
            p.add(q%j)

        if len(total)==len(p):
            print(j)
            break
    
