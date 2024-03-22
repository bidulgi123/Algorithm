import sys
input=sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
total = [[0] for i in range(4)]

for i in a:
    for j in range(5):
        if j == 4:
            print('NO')
            sys.exit()
        if total[j][-1] < i :
            total[j].append(i)
            break
print('YES')