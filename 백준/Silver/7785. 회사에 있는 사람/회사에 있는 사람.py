import sys
input = sys.stdin.readline
office=set()
for i in range(int(input())):
    q=list(map(str,input().split()))
    if q[1] == 'enter' :
        office.add(q[0])
    else :
        office.remove(q[0])
o=sorted(office,reverse=True)
for i in o :
    print(i)