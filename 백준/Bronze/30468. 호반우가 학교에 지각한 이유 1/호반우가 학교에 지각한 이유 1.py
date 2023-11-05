a=list(map(int,input().split()))
mean=a.pop()
if sum(a)//4 < mean :
    print(mean*4-sum(a))
else:
    print(0)