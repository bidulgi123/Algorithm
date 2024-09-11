a, b = map(int, input().split())
if a > b or 26 * a < b :
    print('!')
else :
    total = [0 for i in range(27)]
    while a != 0 :
        if b > 26 and b - 26 > a:
            total[26] += 1
            b -= 26
            a -= 1
        elif b > 0 and a > 1 :
            total[1] += 1
            b -= 1
            a -= 1
        else :
            total[b] +=1 
            b = 0
            a -= 1
    ans = ''
    for i, j in enumerate(total) :
        if j != 0 :
            ans += chr(i + 96) * j
    print(ans.upper())