ans = 0
a = int(input())
num = '1'*len(str(a))
if int(num) < a :
    num+='1'
num=int(num)
while a != 0:
    r = a // num
    a %= num
    ans += r
    num //= 10
print(ans)