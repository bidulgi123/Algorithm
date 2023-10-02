ans=[]
a,b=map(int,input().split())
total=list(map(int,input().split()))
total.append(b)
total=sorted(total)
q=0
for i in range(a+1):
    if b == total[i] :
        ans.append(abs(q-total[i]))
        break
    else :
        ans.append(abs(q-total[i]))
        q=total[i]
print(max(ans))