from collections import deque
a, b, n, m = map(int, input().split())
graph = [float('inf')] * 100001
move = deque()
graph[n] = 1
move.append((n, graph[n]))
while move :
    now, time = move.popleft()
    if now == m : 
        break
    s = [now + 1, now - 1, now + a, now + b, now - a, now - b, now * a, now * b]
    for i in s :
        if i >= 0 and i <= 100000 :
            if graph[i] == float('inf'):
                graph[i] = time + 1
                move.append((i, graph[i]))
print(graph[m] - 1)