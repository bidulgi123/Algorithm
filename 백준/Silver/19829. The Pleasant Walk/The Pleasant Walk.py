from collections import deque
a, b = map(int, input().split())
c = list(map(int, input().split()))
s, e = 0, 1 
d = deque()
d.append(c[0])
l = 1
while e < a :
    if len(d) == 0 :
        d.append(c[s])
    if d[-1] != c[e] :
        d.append(c[e])
        e+=1
        l = max(l, len(d))
    elif d[-1] == c[e] :
        d = deque()
        s = e
        e = s + 1
print(l)
    