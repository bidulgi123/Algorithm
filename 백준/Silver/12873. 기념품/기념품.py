from collections import deque
l = deque(i for i in range(1, int(input()) + 1))
start = 0 
cnt = 1
while len(l) != 1 :
    c = cnt ** 3 % len(l) 
    for i in range(c):
        l.append(l.popleft())
    l.pop()
    cnt +=1 
print(*l)