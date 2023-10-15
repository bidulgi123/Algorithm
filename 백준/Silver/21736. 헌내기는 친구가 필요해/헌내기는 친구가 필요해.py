import sys
sys.setrecursionlimit(1987654321)
input = sys.stdin.readline
a, b = map(int, input().split())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
total = []
for i in range(a):
    q = list(input().rstrip())
    t = set(q)
    if 'I' in t:
        qx = q.index('I')
        qy = i
    total.append(q)
cnt = 0
total[qy][qx] = 'O'
def dfs(y, x):
    global cnt
    if y < 0 or y >= a or x < 0 or x >= b:
        return False
    if total[y][x] == 'P' or total[y][x] == 'O':
        if total[y][x] == 'P':
            cnt += 1
        total[y][x] = '?'
        for dy, dx in move:
            my, mx = y + dy, x + dx
            dfs(my, mx)  
        return True
    return False
dfs(qy, qx)
if cnt == 0 :
    print('TT')
else :
    print(cnt)