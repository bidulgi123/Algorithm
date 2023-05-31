a=int(input())
total=[0] * (a+1)
total[0] = 1
total[1] = 1
for i in range(2,a):
    total[i] = total[i-1] + total[i-2]
print(total[a-1])