import sys
input=sys.stdin.readline
total=set()
for i in range(int(input())):
    c=input().split()
    if c[0] == 'add' :
        total.add(int(c[1]))
    if c[0] == 'check' : 
        if int(c[1]) in total :
            print(1)
        else :
            print(0)
    if c[0] == 'remove':
        if int(c[1]) in total:
            total.remove(int(c[1]))
        else :
            continue
    if c[0] =='toggle':
        if int(c[1]) in total:
            total.remove(int(c[1]))
        else :
            total.add(int(c[1]))
    if c[0] == 'all':
        total=set([i for i in range(1,21)])
    if c[0] == 'empty':
        total=set()
