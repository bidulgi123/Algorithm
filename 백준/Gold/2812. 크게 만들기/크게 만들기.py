import copy
a, b = map(int, input().split())
p = copy.deepcopy(b)
t = list(map(int, input()))
s = [t[0]]
c = 1
while c < a :
    while b > 0 and len(s) != 0 and s[-1] < t[c] :
        s.pop()
        b-=1
    s.append(t[c])
    c+=1
print(*s[:a-p], sep='')