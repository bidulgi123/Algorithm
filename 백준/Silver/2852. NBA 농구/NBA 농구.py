import sys
input = sys.stdin.readline
a = int(input())
score = {'1' : 0, '2' : 0}
total = [list(input().split()) for _ in range(a)]
total.append(['1', '48:00'])
score[total[0][0]] += 1
start = total[0][1].split(':')
start = int(start[0]) * 60 + int(start[1])
team_1 = 0
team_2 = 0
for i in range(1, len(total)):
    mid = total[i][1].split(':')
    mid = int(mid[0]) * 60 + int(mid[1])
    if score['1'] > score['2'] :
        team_1 += mid - start 
    elif score['1'] < score['2'] :
        team_2 += mid - start
    score[total[i][0]] += 1
    start = mid 
minutes = team_1 // 60
seconds = team_1 % 60
print(str(minutes).zfill(2) + ':' + str(seconds).zfill(2)) 
minutes = team_2 // 60
seconds = team_2 % 60
print(str(minutes).zfill(2) + ':' + str(seconds).zfill(2)) 