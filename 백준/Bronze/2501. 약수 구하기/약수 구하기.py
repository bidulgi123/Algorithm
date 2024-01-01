a,b=map(int,input().split())
total=[i for i in range(1,a+1) if a % i ==0]
try:
    print(total[b-1])
except:
    print(0)