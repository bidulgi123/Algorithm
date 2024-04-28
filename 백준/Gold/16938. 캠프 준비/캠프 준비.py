from itertools import combinations
import sys
n, l, r, x = map(int, input().split())
total = list(map(int, input().split()))
cnt = 0
if n == 1 :
    print(0)
    sys.exit()
for i in range(2, n+1):
    com = list(combinations(total, i))
    for j in com:
        if sum(j) >= l and sum(j) <= r and max(j)-min(j) >= x :
            cnt +=1 
print(cnt)