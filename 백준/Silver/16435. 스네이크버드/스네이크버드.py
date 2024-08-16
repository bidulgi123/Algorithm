a,b=map(int,input().split())
t=sorted(list(map(int,input().split())))
for i in t :
    if b >= i :
        b+=1
print(b)
