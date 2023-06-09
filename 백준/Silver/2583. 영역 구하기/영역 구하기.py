import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
m,n,k = map(int,input().split())
total=[[0 for i in range(n)]for i in range(m)]
for i in range(k):
    left_x,left_y,right_x,right_y = map(int,input().split())
    for j in range(left_y,right_y):
        for t in range(left_x,right_x):
            total[j][t] = 1
cnt = 0
def dfs(x,y):
    global cnt
    if x < 0 or x >= n or y >= m or y < 0 :
        return False
    if total[y][x] == 0 :
        total[y][x] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        cnt+=1
        return True
    return False
ans=[]
for i in range(m) :
    for j in range(n):
        if dfs(j,i)==True:
            ans.append(cnt)
            cnt=0
print(len(ans))
print(*sorted(ans))