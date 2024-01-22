a,b=map(int,input().split())
cnt=0
t=0
while cnt != a : 
    t+=1
    if str(b) in str(t):
        continue
    else :
        cnt+=1
print(t)