import sys
a=input()
for i in ['pi','ka','chu']:
    if i in a :
        a=a.replace(i,'?')
for i in a :
    if i != '?' :
        print('NO')
        sys.exit()
print('YES')