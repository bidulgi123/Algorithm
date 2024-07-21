import sys
input = sys.stdin.readline
while True:
    a, b = map(int, input().split())
    if a == b and a == 0 :
        break
    total = [list(input().rstrip()) for i in range(a)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    for i in range(a):
        middle = []
        for j in range(b):
            cnt = 0
            if total[i][j] == '.' :
                for dx, dy in move :
                    rx = i + dx
                    ry = j + dy
                    if rx >= 0 and rx < a and ry >= 0 and ry < b :
                        if total[rx][ry] == '*' :
                            cnt+=1
                middle.append(cnt)
            else :
                middle.append('*')
        print(*middle, sep='')