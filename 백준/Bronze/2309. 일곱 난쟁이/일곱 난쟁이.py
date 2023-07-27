from itertools import combinations
a=[int(input()) for i in range(9)]
for j in list(combinations(a,7)):
  if sum(j) == 100 :
    o=list(j)
    o.sort()
    for q in o :
      print(q)
    break