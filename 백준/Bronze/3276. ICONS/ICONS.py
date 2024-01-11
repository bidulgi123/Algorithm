a,b=1,1
c=int(input())
while a * b < c:
    if a > b : 
        b+=1
    else : 
        a+=1
print(a,b)