import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[list(input().rstrip()) for i in range(b)]
cnt=0
p=[]
q=[]
def dfs(i,j,o):
    global cnt
    if i >= b or i < 0 or j >= a or j < 0 :
        return False
    if total[i][j] == o:
        total[i][j] = '?'
        dfs(i+1,j,o)
        dfs(i-1,j,o)
        dfs(i,j+1,o)
        dfs(i,j-1,o)
        cnt+=1
        return True
    return False
for i in range(a) :
    for j in range(b):
        if dfs(j,i,'W')==True:
            p.append(cnt**2)
            cnt=0
        if dfs(j,i,'B')==True:
            q.append(cnt**2)
            cnt=0
print(sum(p),sum(q))