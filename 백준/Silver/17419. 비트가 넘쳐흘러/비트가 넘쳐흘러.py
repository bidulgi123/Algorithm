input()
a = int(input(), 2)
ans = 0
while a != 0:
  a = a - (a&((~a)+1))
  ans += 1
print(ans)