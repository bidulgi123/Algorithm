a= int(input())
ans= 0
b = 1
while a > 0 :
  if a < b :
    b = 1
  a -= b
  b += 1
  ans += 1
print(ans)