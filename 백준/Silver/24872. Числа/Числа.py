import sys
a=int(input())
b=int(input())
if b == 0 :
    while True :
        if len(set(list(str(a)))) == 1:
            print(a)
            break
        a+=1
else :
    while True :
        if len(set(list(str(a)))) <= 2:
            print(a)
            break
        a+=1