import sys
from collections import deque
input = sys.stdin.readline
ans = 0
a, b = map(int, input().split())
c = deque(map(int, input().split()))
robot = deque([0] * a)
cnt = 0

while True :
    ans += 1
    c.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0

    for i in range(a - 2, -1, -1):  
        if c[i + 1] > 0 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            c[i + 1] -= 1
            if c[i + 1] == 0:
                cnt +=1

    robot[-1] = 0  

    if c[0] != 0 and robot[0] != 1:
        robot[0] = 1
        c[0] -= 1
        if c[0] == 0 :
            cnt +=1 
    
    if cnt >= b:
        break

print(ans)