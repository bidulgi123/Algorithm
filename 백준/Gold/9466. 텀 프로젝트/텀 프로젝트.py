import sys
sys.setrecursionlimit(9**9)
input = sys.stdin.readline

def dfs(c):
    global ans
    visit[c] = 1
    move.append(c)
    ss = point[c - 1]
    if visit[ss] == 1 :
        if ss in move : 
            ans += len(move[move.index(ss):])
    else :
        dfs(ss)

for _ in range(int(input())):
    ans = 0
    n = int(input())
    point = list(map(int, input().split()))
    visit = [0] * (n + 1)

    for s in range(1, n + 1):
        if visit[s] != 1:
            move = []
            dfs(s)

    print(n - ans)