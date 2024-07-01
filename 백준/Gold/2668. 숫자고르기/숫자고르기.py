def bfs(i, s):
    visited[i] = 1
    mid = total[i]
    if visited[mid] == 0 :
        bfs(mid, s)
    elif visited[mid] == 1 and s == mid:
        ans.append(mid)
a = int(input())
total = [0] + [int(input()) for i in range(a)]
ans = []
for j in range(1, a+1):
    visited = [0] * (a + 1)
    bfs(j, j)
print(len(ans))
print(*sorted(set(ans)), sep='\n')