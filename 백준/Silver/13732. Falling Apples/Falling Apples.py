import sys
input = sys.stdin.readline 
a, b = map(int, input().split())
total = [list(input().rstrip()) for i in range(a)]
ans = []
for i in range(b):
    cnt = 0
    no = 0
    mid = ''
    for j in range(a):
        if total[j][i] == 'a' :
            cnt += 1
        elif total[j][i] == '#' :
            mid += '.'*no+'a'*cnt+total[j][i]
            cnt = 0
            no = 0
        else : 
            no += 1
    if cnt != 0 or no != 0 :
        mid += '.'*no+'a'*cnt
    ans.append(mid)
ans = [list(row) for row in ans]
ans = list(map(list, zip(*ans)))
for i in ans :
    print(*i, sep='')