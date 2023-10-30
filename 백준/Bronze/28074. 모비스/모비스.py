a = input()
r=-1
for i in 'MOBIS' :
    if i not in a :	
        r = 0
        break
if r == 0 :
    print('NO')
else :
    print('YES')