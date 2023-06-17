import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i,j):
    global cnt
    if i < 0 or i >=a or j < 0 or j >=b :
        return False
    if total[i][j] == '#':
        total[i][j] = 'q'
        cnt+=1
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        dfs(i-1,j)
        return True
    return False
a,b,c=map(int,input().split())
ans=0
cnt=0
total=[['.']*b for i in range(a)]
for j in range(c):
    x, y = map(int, input().split())
    total[x-1][y-1] = '#'
for i in range(a):
    for j in range(b):
        if dfs(i,j) == True:
            if cnt > ans :
                ans=cnt
        cnt=0
print(ans)