from itertools import *
a = int(input())
t = list(permutations([0,1,2,3,4,5,6,7,8,9], a+1))
q = list(map(str, input().split()))
ans_list = []
for i in t :
    for j in range(a) :
        if q[j] == '<' and i[j] > i[j+1]:
            break
        if q[j] == '>' and i[j] < i[j+1]:
            break
        if j == a -1 :
            ans_list.append(i)
print(*ans_list[-1], sep='')
print(*ans_list[0], sep='')