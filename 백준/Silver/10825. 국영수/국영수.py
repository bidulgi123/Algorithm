import sys
input = sys.stdin.readline
total = []
for i in range(int(input())):
    m = list(input().split())
    for j in range(1, 4):
        m[j] = int(m[j])
    total.append(m)
total.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in total :
    print(i[0])