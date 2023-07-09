import sys
input=sys.stdin.readline
a=input()
flag=0
for i in a :
    if i == 'U' and flag ==0:
        flag=1
    if i =='C' and flag == 1 :
        flag = 2
    if i == 'P' and flag == 2 :
        flag = 3
    if i == 'C' and flag == 3 :
        flag = 4
if flag == 4 :
    print("I love UCPC")
else :
    print("I hate UCPC")
        