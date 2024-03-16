a=input()
b=input()
ans=''
for i, j in zip(a,b):
    if int(i) >= int(j) :
        ans+=i
    else :
        ans+=j
print(ans)