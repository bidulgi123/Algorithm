a = int(input())
p = 10000000 
t = [1 for _ in range(p)]  
s = []  
for i in range(2, p):
    if t[i] == 1:  
        s.append(i) 
        for j in range(i * i, p, i):  
            t[j] = 0 
    if len(s) == a: 
        break
print(s[-1])
