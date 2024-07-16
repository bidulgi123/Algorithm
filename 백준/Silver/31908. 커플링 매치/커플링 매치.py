import sys
input = sys.stdin.readline
total = {}
for i in range(int(input())):
    b, c = map(str, input().split())
    if c != '-' :
        if c not in total : 
            total[c] = [[b], 1]
        else :
            total[c][0].append(b)
            total[c][1] += 1
ans = [v for k, v in total.items() if v[1] == 2] 
if len(ans) != 0 :
    print(len(ans))
    for i in ans :
        print(*i[0])
else :
    print(0)