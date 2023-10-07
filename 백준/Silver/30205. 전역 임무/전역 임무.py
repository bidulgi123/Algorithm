import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
item=0
clear=1
for j in range(a):
    floor = list(map(int,input().split()))
    floor.sort()
    for i in floor :
        if i == -1 :
            item+=1
        if c >= i and i >= 0: 
            c+=i
        elif c < i :
            if c * (2**item) >= i :
                while True:
                    if c >= i : 
                        break
                    else :
                        c=c*2
                        item-=1
                c+=i
            else :
                print(0)
                sys.exit()  
    if item != 0 :
        for q in range(item):
            c=c*2
    item = 0 
print(clear)