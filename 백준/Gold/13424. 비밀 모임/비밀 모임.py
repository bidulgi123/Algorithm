import sys
INF = float('inf')
input = sys.stdin.readline
a = int(input())
for _ in range(a):
    n, m = map(int, input().split())
    node = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        s, e, w = map(int, input().split())
        if node[s][e] > w :
            node[s][e] = w
        if node[e][s] > w :
            node[e][s] = w

    for k in range(1,n+1):
        node[k][k]=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                node[i][j] = min(node[i][j], node[i][k] + node[k][j])

    input()
    friend = list(map(int, input().split()))
    min_sum = INF
    ans = -1
    for p in range(1, n + 1):
        total = 0
        for fri in friend :
            total += node[p][fri]
        if min_sum > total :
            ans = p
            min_sum = total
    print(ans)