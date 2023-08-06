a = input()
b = input()
total = [0]*26
for s in a:
    total[ord(s)-97] += 1
for s in b:
    total[ord(s)-97] -= 1
ans=0
for i in total:
    ans += abs(i)
print(ans)