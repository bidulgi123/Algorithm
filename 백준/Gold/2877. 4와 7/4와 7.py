a = int(input())
ans =''
while a > 0:
    b = a % 2 
    a //= 2
    if b == 0: 
        a -= 1 
        ans = '7' + ans
    else: 
        ans = '4' + ans
print(ans)