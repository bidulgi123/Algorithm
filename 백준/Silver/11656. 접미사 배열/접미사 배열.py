a=input()
b=set()
for i in range(len(a)):
    b.add(a[i:])
b=sorted(b)
print(*b, sep='\n')