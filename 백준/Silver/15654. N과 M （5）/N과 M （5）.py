from itertools import permutations 
a, b = map(int, input().split())
t=list(map(int, input().split()))
total=sorted(list(permutations(t, b)))
for i in range(len(total)):
    print(*total[i])