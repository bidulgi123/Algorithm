import sys
from itertools import combinations
input = sys.stdin.readline
total=[]
for j in range(int(input())):
  a=list(map(int,input().split()))
  score=0
  for i in set(combinations(a,3)):
      str_i=str(sum(i))
      str_i_end=str_i[-1]
      score=max(int(str_i_end),score)
  total.append((score,j+1))
total.sort(reverse=True)
print(total[0][1])