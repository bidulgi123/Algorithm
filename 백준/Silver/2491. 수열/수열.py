a=int(input())
c=list(map(int, input().split()))
cnt=1
if a!= 1:
    b=[0]*(a+1)
    for i in range(1,a):
        if c[i] >= c[i-1] :
            cnt+=1
            b[i] = cnt
        else :
            b[i] = cnt
            cnt=1
    p=[0]*(a+1)    
    cnt=1
    for i in range(1,a):
        if c[i] <= c[i-1] :
            cnt+=1
            p[i] = cnt
        else :
            p[i] = cnt
            cnt=1
    print(max(max(p),max(b)))
else :
    print(1)