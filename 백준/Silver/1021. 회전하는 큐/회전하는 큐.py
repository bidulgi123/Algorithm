from collections import deque
a, b = map(int,input().split())
c=deque(map(int, input().split()))
total=deque(i for i in range(1,a+1))
cnt=0
while len(c) != 0 :
    if total[0] == c[0]:
        total.popleft()
        c.popleft()
        continue
    if total.index(c[0]) <= len(total) // 2 :
        total.append(total.popleft())
        cnt+=1
    else :
        total.appendleft(total.pop())
        cnt+=1
print(cnt)