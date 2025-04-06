import sys
input = sys.stdin.readline
a = int(input())
total = [list(input()) for _ in range(a)]
move_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(1, a - 1):
    for j in range(1, a -1):
        if all(total[x][y] == '*' for x, y in [(i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]):
            coronary = (i, j)

left_point = coronary[1]
left_length = 0
right_point = coronary[1]
right_length = 0
body_point = coronary[0]
body_length = 0

while left_point < a: 
    left_point -= 1 
    if total[coronary[0]][left_point] == '*':
        left_length += 1
    else :
        break

while right_point < a: 
    right_point += 1 
    if total[coronary[0]][right_point] == '*':
        right_length += 1
    else :
        break

while body_point < a:    
    body_point += 1
    if total[body_point][coronary[1]] == '*':
        body_length += 1
    else :
        break

left_leg_point = body_point
left_leg_length = 0
right_leg_point = body_point
right_leg_length = 0

while right_leg_point < a:    
    if total[right_leg_point][coronary[1]+1] == '*':
        right_leg_length += 1
    else :
        break
    right_leg_point += 1

while left_leg_point < a:    
    if total[left_leg_point][coronary[1]-1] == '*':
        left_leg_length += 1
    else :
        break
    left_leg_point += 1

print(coronary[0]+1, coronary[1]+1)
print(left_length, right_length, body_length, left_leg_length, right_leg_length)