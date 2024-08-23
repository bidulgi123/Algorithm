a, b = map(int, input().split())
c = list(map(int, input().split()))
s, e = 0, 1 
d = c[s]
l = 1
cnt = 1
while e < a :
    if d != c[e] :
        d = c[e]
        e+=1
        cnt += 1
        l = max(l, cnt)
    elif d == c[e] :
        d = c[e]
        s = e
        e = s + 1
        cnt = 1
print(l)