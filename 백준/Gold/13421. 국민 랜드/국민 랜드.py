import sys
import itertools
input = sys.stdin.readline

total = [tuple(map(int, input().split())) for _ in range(4)]
signs = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

def rand(length):
    square = [(length * dx, length * dy) for dx, dy in signs]
    min_move = float('inf')

    for order in itertools.permutations(range(4)):
        move = 0
        for i in range(4):
            x1, y1 = total[order[i]]
            x2, y2 = square[i]
            move += abs(x1 - x2) + abs(y1 - y2)
        min_move = min(min_move, move)

    return min_move

left = 0
right = 10**9

while right - left >= 3:
    left_third = left + (right - left) // 3
    right_third = right - (right - left) // 3
    if rand(left_third) < rand(right_third):
        right = right_third
    else:
        left = left_third

ans = float('inf')
length = 0
for t in range(left, right + 1):
    w = rand(t)
    if w <= ans:
        ans = w
        length = t

if length * 2 == 0 :
    print(1)
else :
    print(length * 2)