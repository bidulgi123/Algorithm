a=int(input())
total=[1]*(a+2)
total[1]=3
total[2]=7
for i in range(3,a+1):
    total[i] = (total[i-1]*2+total[i-2])%9901
print(total[a])
