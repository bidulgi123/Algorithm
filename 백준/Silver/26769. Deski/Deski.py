a=int(input())
b=list(map(int,input().split()))
b=sorted(b,reverse=True)
try:
    print(b[3]**2)
except:
    print(0)