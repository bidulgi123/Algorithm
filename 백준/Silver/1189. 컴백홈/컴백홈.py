import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
total=[list(input()) for i in range(a)]
move=[(1,0),(-1,0),(0,1),(0,-1)]
ans=0
def dfs(x,y,dis):
    global ans
    if dis == c and x == 0 and y == b-1:
        ans+=1 
    else :
        total[x][y] = 'T'
        for i in move:
            nx = x+i[0]
            ny = y+i[1]
            if nx >= 0 and ny >= 0 and nx < a and ny < b :
                if total[nx][ny] != 'T':
                    total[nx][ny] = 'T'
                    dfs(nx,ny,dis+1)
                    total[nx][ny] = '.'
        
dfs(a-1,0,1)
print(ans)