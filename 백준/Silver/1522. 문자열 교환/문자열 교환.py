a = input()
cnt = a.count('a')
a += a 
ans = float('inf')
for i in range(len(a)-cnt):
    ans = min(ans, a[i:i+cnt].count('b'))
print(ans)