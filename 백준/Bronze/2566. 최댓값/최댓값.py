total = [list(map(int,input().split())) for i in range(9)]
p=0
start, end = 1, 1
for i in range(9):
    for j in range(9):
        if p < total[i][j] :
            p = total[i][j]
            start = i + 1
            end = j + 1
print(p)
print(start, end)