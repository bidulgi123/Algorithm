import sys
import heapq
input = sys.stdin.readline

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dj(size):
    visited = [[float('inf')] * size for _ in range(size)]
    visited[0][0] = total[0][0]
    h = []
    heapq.heappush(h, (total[0][0], 0, 0))  

    while h:
        w, y, x = heapq.heappop(h)

        if visited[y][x] < w:
            continue

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < size and 0 <= nx < size:  
                new_cost = w + total[ny][nx]
                if visited[ny][nx] > new_cost:  
                    visited[ny][nx] = new_cost
                    heapq.heappush(h, (new_cost, ny, nx))

    return visited[size-1][size-1]  

cnt = 0
while True:
    cnt +=1 
    a = int(input())
    if a == 0:
        break
    total = [list(map(int, input().split())) for _ in range(a)]
    print(f'Problem {cnt}: {dj(a)}')
