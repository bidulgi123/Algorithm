import sys
input = sys.stdin.readline
a = int(input())
total = [list(input().rstrip()) for i in range(a)]
ans = []
for i in range(a):
    q = 0
    mid = []
    for j in range(a):
        q = 0
        for b in range(i-1, i+2):
            for c in range(j-1, j+2):
                if b >= 0 and b < a and c >= 0 and c < a :
                    if total[b][c] != '.':
                        q += int(total[b][c])
        if total[i][j] == '.':
            if q < 10 :
                mid.append(str(q))
            else :
                mid.append('M')
        else :
            mid.append('*')
    ans.append(mid)
for text in ans :
    print(*text, sep='')