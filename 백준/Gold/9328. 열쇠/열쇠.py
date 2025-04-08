import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    start_point = []
    h, w = map(int, input().split())
    graph = []

    for y in range(h):
        load = list(input().rstrip())
        if y == 0 or y == h - 1:
            for x in range(w):
                if load[x] != '*':
                    start_point.append((y, x, load[x]))
        else:
            if load[0] != '*':
                start_point.append((y, 0, load[0]))
            if load[-1] != '*':
                start_point.append((y, w - 1, load[-1]))
        graph.append(load)

    key_input = input().strip()
    
    if key_input == '0' :
        key = set()
    else :
        key = set(map(str.upper, key_input))

    key.add('.') 

    visited = [[-1] * w for _ in range(h)]
    q = deque()
    check_list = dict()  

    for y, x, val in start_point:
        if graph[y][x] != '*':
            q.append((y, x))
            visited[y][x] = 1

    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    answer = 0

    while q:
        y, x = q.popleft()

        cell = graph[y][x]
        if 'a' <= cell <= 'z': 
            upper_key = cell.upper()
            if upper_key not in key:
                key.add(upper_key)
                
                if upper_key in check_list:
                    for pos in check_list[upper_key]:
                        q.append(pos)
                    del check_list[upper_key]
        elif 'A' <= cell <= 'Z':  
            if cell not in key:
                if cell not in check_list:
                    check_list[cell] = []
                check_list[cell].append((y, x))
                continue  

        elif cell == '$': 
            answer += 1

        graph[y][x] = '.'  

        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if visited[ny][nx] == -1 and graph[ny][nx] != '*':
                    visited[ny][nx] = 1
                    q.append((ny, nx))

    print(answer)