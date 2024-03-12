from collections import deque
a,b=map(int,input().split())
q=deque([a])
v={a:0}
while q:
    c=q.popleft()
    if c==b:
        break
    else :
        for x in [2*c,c+1]:
            if x in v or x>b:
                continue
            else :
                v[x]=v[c]+1
                q.append(x)
print(v[b])