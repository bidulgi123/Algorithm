import sys
input = sys.stdin.readline
a = int(input())
for __ in range(1,a+1):
    x, y, t = map(int, input().split())
    total = [[0]*y for i in range(x)]
    cnt = x * y - t
    for _ in range(t):
        j, k =map(int, input().split())
        total[j][k] = 1
    search = min(x, y)
    for i in range(2, search+1):
        for n in range(y-i+1):
            for u in range(x-i+1):
                q = total[u][n:n+i]
                for pp in range(i):
                    q += total[u+pp][n:n+i]
                if 1 not in q :
                    cnt+=1
    print(f"Case #{__}:",cnt)