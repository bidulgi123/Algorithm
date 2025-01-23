import sys
input = sys.stdin.readline
a, b = map(int, input().split())
graph = [int(input()) for _ in range(a)]
graph.sort()
start, end = 1, graph[-1] - graph[0]
while start <= end:
    mid = (start + end) // 2
    current = graph[0]
    cnt = 1
    for i in range(1, a):
        if graph[i] - mid >= current:
            cnt += 1
            current = graph[i]
    if cnt >= b:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)