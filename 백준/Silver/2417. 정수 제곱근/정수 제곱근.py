a = int(input())
s = 0
e = a
while s <= e:
    mid = (s + e) // 2
    if mid ** 2 < a:
        s = mid + 1
    else:
        e = mid - 1
print(s)