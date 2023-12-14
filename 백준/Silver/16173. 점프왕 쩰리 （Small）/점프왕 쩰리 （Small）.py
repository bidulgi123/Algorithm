import sys
input=sys.stdin.readline
a=int(input())
total=[list(map(int,input().split())) for i in range(a)]
visited=[[0] * a for i in range(a)]
def dfs(x,y):
    if x < 0 or x >=a or y >= a or y < 0 or visited[x][y] == 1 :
        return False 
    if total[x][y] == -1 :
        visited[x][y] = 1 
        return True 
    visited[x][y] = 1 
    move=[(0,total[x][y]),(total[x][y],0)]
    for i in move :
        mx=x+i[0]
        my=y+i[1]
        dfs(mx,my)
dfs(0,0)
if visited[a-1][a-1] == 1 :
    print("HaruHaru")
else :
    print("Hing")