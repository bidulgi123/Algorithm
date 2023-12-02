from collections import deque
a,b=map(int,input().split())
c=list(input())
cnt=0
total=0
for i in range(b):
    if c[i] == 'L':
        cnt+=1
total=max(cnt,total)
ans=1
p=1
for j in range(b,len(c)):
    p+=1
    if c[j - b] == 'L':
        cnt-=1
    if c[j] == 'L':  
        cnt+=1
    if cnt > total : 
        total=cnt
        ans=p
print(ans)