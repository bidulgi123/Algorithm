input()
a = input()
t = set(['1','2','3','4','5','6','7','8','9','0'])
ans = 0
mid = '0'
for i in a :
    if str(i) in t :
            mid += i
    else :
        ans += int(mid)
        mid = '0'
ans += int(mid)
print(ans)