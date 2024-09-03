import sys
input = sys.stdin.readline
a, b = map(int, input().split())
jawon = list(map(int, input().split()))
total = []
j_s = sum(jawon)
for i in range(1, a+1):
    q = list(map(int, input().split()))
    s = sum(q)
    if s <= j_s :
        q.append(sum(q))
        q.append(i)
        total.append(q)
total.sort(key=lambda x : x[3], reverse=True)
print(0, end= ' ')
try :
    for j in range(b - 1):
        print(total[j][4], end=' ')
except :
    print()