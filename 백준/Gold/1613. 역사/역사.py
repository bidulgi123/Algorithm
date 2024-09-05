import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())
total=[[0]*(a+1) for _ in range(a+1)]   
for i in range(b):
    c, d = map(int, input().split())
    total[c][d] = 1
for k in range(1, a + 1):
    for t in range(1, a + 1):
        for q in range(1, a + 1):
            if total[t][k] + total[k][q] == 2:
                total[t][q] = 1 
for _ in range(int(input())):
    a, b = map(int, input().split())
    if total[a][b] == 1 and total[b][a] == 0 :
        print(-1)
    elif total[a][b] == 0 and total[b][a] == 1 :
        print(1)
    else :
        print(0)