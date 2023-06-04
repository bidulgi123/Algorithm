a,c,d=map(int, input().split())
b=list(map(int, input().split()))
b.append(0)
b.append(0)
cnt=0

if min(c,d) == d : 
    for i in range(len(b)-2):
        if b[i+1] > b[i+2] and b[i+2] != 0 :
            m = min(b[i+1]-b[i+2],b[i])
            cnt+=m*(c+d)
            b[i] = b[i] - m
            b[i+1] = b[i+1] - m
        if b[i+2] > 0 and b[i+1] > 0 and b[i] > 0 :
            m = min(b[i],b[i+1],b[i+2])
            cnt+=m*(c+2*d)
            b[i] = b[i] - m
            b[i+1] = b[i+1] - m
            b[i+2] = b[i+2] - m
        if b[i] != 0 and b[i+1] != 0 and b[i+2] == 0 :
            m = min(b[i],b[i+1])
            cnt+=m*(c+d)
            b[i] = b[i] - m
            b[i+1] = b[i+1] - m
        if b[i] != 0 :
            cnt+=b[i]*c
            b[i]=0
else:
    for i in range(len(b)-2):
        if b[i] != 0 :
            cnt+=b[i]*c
            b[i]=0    
        
print(cnt)