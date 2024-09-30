from collections import deque
a, b = map(int, input().split())
graph = [float('inf')] * 100001
m = deque()
graph[a] = 1
m.append((a, graph[a]))
while m :
    now, time = m.popleft()
    if now == b :
        break
    move = [now + 1, now - 1]
    for i in move :
        if i >= 0 and i <= 100000 :
            if graph[i] > time + 1 :
                graph[i] = time + 1
                m.append((i, graph[i]))
    if now * 2 >= 0 and now * 2 <= 100000 :
        if graph[now * 2] > time :
            graph[now * 2] = time
            m.append((now * 2, time))
print(graph[b] - 1)