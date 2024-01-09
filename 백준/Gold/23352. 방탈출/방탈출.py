import sys
from collections import deque 
import copy
input=sys.stdin.readline
y,x=map(int,input().split())
total=[list(map(int, input().split())) for i in range(y)]
visited=[[0]*x for _ in range(y)]
move=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(i,j):
    total_copy=copy.deepcopy(total)
    visited_copy=copy.deepcopy(visited)
    q=deque()
    q.append([i,j])
    s=total_copy[i][j]
    total_copy[i][j]=0
    e=0
    while q :
        y_1, x_1 = q.popleft()
        for i in move:
            y_2 = y_1 + i[0]
            x_2 = x_1 + i[1]
            if y_2 >= 0 and y_2 < y and x_2 >= 0 and x_2 < x and visited_copy[y_2][x_2] == 0 and total_copy[y_2][x_2] != 0 :
                visited_copy[y_2][x_2]=visited_copy[y_1][x_1]+1
                q.append([y_2,x_2])
                e=total_copy[y_2][x_2]
    return s,e,max(map(max, visited_copy))
dis=0
answer=0
ans=[]
for y_move in range(y):
    for x_move in range(x):
        if total[y_move][x_move] != 0 :
            start,end,moving=bfs(y_move,x_move)
            ans.append((start,end,moving))
            if moving > dis :
                dis = moving
for L in ans :
    if L[0] + L[1] > answer and L[2] == dis :
        answer=L[0] + L[1]
print(answer)