import math
a, b = map(int, input().split())  
total = list(map(int, input().split()))
dif = [math.inf] * a 
for i in range(a - 1):
    dif[i] = total[i + 1] - total[i]
dif.sort()
s = 0
for i in range(a - b):
    s += dif[i]
print(s)        