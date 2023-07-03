import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
a,b=map(int,input().split())
total=[]
for i in range(a):
    total.append(list(map(int, input().split())))
m=[]
def dfs(x,y):
    global cnt
    if x<=-1 or x>= a or y>= b or y<=-1 :
        return False 
    if total[x][y] == 1 :
        total[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        cnt+=1
        m.append(cnt)
        return True
    return False
re=0
for q in range(a):
    for t in range(b):
        cnt=0
        if dfs(q,t) == True:
            re+=1
print(re)
try :
    print(max(m))
except :
    print(0)