a = int(input())
b = list(map(int, input().split()))
start, end = 0, 0
ans = 0
c = dict()
while end < a:
    c[b[end]] = c.get(b[end], 0) + 1
    while len(c) > 2:
        c[b[start]] -= 1
        if c[b[start]] == 0:
            del c[b[start]]
        start += 1
    if len(c) == 2 :
        ans = max(ans, end - start + 1)
    end += 1
ans = max(ans, end - start)
print(ans)