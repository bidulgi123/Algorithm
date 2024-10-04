a, b = map(int, input().split())
c = list(map(int, input().split()))
t = [[0] * b for _ in range(a)]
for idx, count in enumerate(c):
    for row in range(count):
        t[row][idx] = 1
ans = 0
for i in range(a):
    middle = 0
    counting = False
    for j in range(b):
        if t[i][j] == 1:
            if counting:
                ans += middle  
            counting = True
            middle = 0 
        elif counting:
            middle += 1  
print(ans)