import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
a = int(input())
total = [list(input().rstrip()) for i in range(a)]
total_rgb = copy.deepcopy(total)
def dfs(x,y, start):
    if x < 0 or x >= a or y >= a or y < 0 :
        return False
    if total[x][y] == start and total[x][y] != '?' :
        total[x][y] = '?'
        dfs(x-1,y,start)
        dfs(x,y-1,start)
        dfs(x+1,y,start)
        dfs(x,y+1,start)
        return True
    return False
cnt = 0
for i in range(a) :
    for j in range(a):
        if dfs(j,i,total[j][i])==True:
            cnt += 1
        if total_rgb[i][j] =='G' :
            total_rgb[i][j] ='R'
cnt_rgb = 0
total = total_rgb
for i in range(a) :
    for j in range(a):
        if dfs(j,i,total[j][i])==True:
            cnt_rgb += 1
print(cnt, cnt_rgb)