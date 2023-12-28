a,b=map(int, input().split())
d,c=map(int, input().split())
e=b-a
f=c-d
while True:
    if e == f:
        break
    if e < f :
        e += b
    else : f += c
print(f)