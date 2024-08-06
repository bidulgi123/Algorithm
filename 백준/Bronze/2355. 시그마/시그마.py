a,b=map(int,input().split())
if b>a:
    b,a=a,b
print(int((a+b)*(a-b+1)/2))