def palindrome(n):
    s = str(n)
    l = len(s)
    if '9' * l == s:
        return n + 2
    if l == 1:
        return n + 1
    h = s[:(l + 1) // 2]
    if l % 2 == 0:
        t = int(h + h[::-1])
    else:
        t = int(h + h[-2::-1])
    if t > n:
        return t
    h = str(int(h) + 1)
    if l % 2 == 0:
        t = int(h + h[::-1])
    else:
        t = int(h + h[-2::-1])
    return t
a = int(input())
print(palindrome(a))
