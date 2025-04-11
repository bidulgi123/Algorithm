import sys
input = sys.stdin.readline
a = int(input())
mouse = [list(map(int, input().split())) for _ in range(a)]

def cage(time):
    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    for x, y, vx, vy in mouse:
        new_x = x + vx * time
        new_y = y + vy * time
        min_x = min(min_x, new_x)
        max_x = max(max_x, new_x)
        min_y = min(min_y, new_y)
        max_y = max(max_y, new_y)

    return max(max_x - min_x, max_y - min_y)

left = 0
right = 2000

while True :
    left_third = left + (right - left) / 3 
    right_third = right - (right - left) / 3 

    if right - left < 1e-12 :
        break

    if cage(left_third) > cage(right_third) :
        left = left_third

    else :
        right = right_third

print(f'{cage(left)}')