a=int(input())
b=[0] * a
b[0]=1
if a > 1 :
    b[1]=2
    for i in range(2,a):
        b[i] = (b[i-1]+b[i-2])%15746
    print(b[-1])
else :
    print(1)