from itertools import combinations, permutations

t, num1 = map(int, input().split())
chick_x_y = []
home_x_y = []
for i in range(t):
    coordinate = list(map(int, input().split()))
    for j in range(len(coordinate)) :
        if coordinate[j] == 1 :
            home_x_y.append([j+1, i+1])
        if coordinate[j] == 2 :
            chick_x_y.append([j+1, i+1])
total = []
for i in range(len(chick_x_y)):
    s = []
    for j in range(len(home_x_y)):
        q = abs(chick_x_y[i][0] - home_x_y[j][0])
        t = abs(chick_x_y[i][1] - home_x_y[j][1])
        p = q+t
        s.append(p)
    total.append(s)
com = list(combinations(total, num1))
toa = []
for i in range(len(com)):
    to = []
    for j in range(len(com[0][0])):
        middle = []
        for p in range(num1):
            middle.append(com[i][p][j])
        to.append(min(middle))
    toa.append(to)
answer = []
for ui in range(len(toa)):
    answer.append(sum(toa[ui]))
print(min(answer))