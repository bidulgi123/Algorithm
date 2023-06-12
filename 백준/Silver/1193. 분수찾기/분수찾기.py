a = int(input())
b = 1
while a > b:
    a -= b
    b += 1
if b%2==0:
    c=a
    d=b-a+1
else:
    c=b-a+1
    d=a
print(str(c)+"/"+str(d))