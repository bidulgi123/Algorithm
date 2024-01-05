import sys
input=sys.stdin.readline
a=0
start=0
q=int(input())
while True:
    start+=1
    q-=len(str(start))
    if q <= 0 :
        print(str(start)[len(str(start))-1+q])
        break
