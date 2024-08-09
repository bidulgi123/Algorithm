from collections import deque
a, b = map(int, input().split())
t = deque(i for i in range(1, a+1))
start = 0 
while len(t) > b :
    t.append(t.popleft())
    for i in range(start + 1, start + b):
        t.popleft()
print(t[0])