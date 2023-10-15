import sys
input=sys.stdin.readline
sys.setrecursionlimit(1987654321)
move = [(0, 1),(0, -1),(1, 0),(-1, 0)]
def dfs(y,x):
    if y >= b or y < 0 or x >= c or x < 0 :
        return False
    if total[y][x] == '#':
        total[y][x] = '?'
        for dy, dx in move:
            ny, nx = y + dy, x + dx,
            dfs(ny,nx)
        return True
    return False
a=int(input())
for i in range(a):
    cnt=0
    b,c=map(int,input().split())
    total=[list(input().rstrip())for i in range(b)]
    for i in range(b):
        for j in range(c):
            if dfs(i,j) == True:
                cnt+=1
    print(cnt)