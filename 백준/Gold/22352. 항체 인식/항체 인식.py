import sys
input = sys.stdin.readline
a, b = map(int, input().split())
first = [list(map(int, input().split())) for i in range(a)]
end = [list(map(int, input().split())) for i in range(a)]
s, e = -1, -1
for i in range(a):
    for j in range(b):
        if first[i][j] != end[i][j] :
            s = i
            e = j
            start = first[i][j]
            last = end[i][j]
            break
    if s != -1 :
        break
def dfs(x, y):
    if x < 0 or x >= a or y >= b or y < 0 :
        return False
    if first[x][y] == start :
        first[x][y] = last
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False
if s == -1 :
    print('YES')
else :
    dfs(s, e)
    if first == end :
        print('YES')
    else :
        print('NO')