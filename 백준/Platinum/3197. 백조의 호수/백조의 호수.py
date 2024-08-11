from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
total = []
swan = []

for i in range(a):
    middle = list(input().rstrip())
    total.append(middle)
    for j in range(b):
        if middle[j] == 'L':
            swan.append((i, j))

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
water_queue = deque()
next_water_queue = deque()
swan_queue = deque([swan[0]])
next_swan_queue = deque()

visited = [[False] * b for _ in range(a)]
swan_visited = [[False] * b for _ in range(a)]
swan_visited[swan[0][0]][swan[0][1]] = True
total[swan[0][0]][swan[0][1]] = '.'
total[swan[1][0]][swan[1][1]] = '.'

for i in range(a):
    for j in range(b):
        if total[i][j] == '.':
            water_queue.append((i, j))
            visited[i][j] = True

def ice_break():
    while water_queue:
        x, y = water_queue.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                if total[nx][ny] == 'X':
                    total[nx][ny] = '.'
                    next_water_queue.append((nx, ny))
                visited[nx][ny] = True

def move_swan():
    while swan_queue:
        x, y = swan_queue.popleft()
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < a and 0 <= ny < b and not swan_visited[nx][ny]:
                if total[nx][ny] == '.':
                    swan_queue.append((nx, ny))
                elif total[nx][ny] == 'X':
                    next_swan_queue.append((nx, ny))
                swan_visited[nx][ny] = True
                if (nx, ny) == swan[1]:
                    return True
    return False

days = 0
while True:
    if move_swan():
        print(days)
        break
    ice_break()
    water_queue, next_water_queue = next_water_queue, deque()
    swan_queue, next_swan_queue = next_swan_queue, deque()
    days += 1
