a = int(input())
q=[]
for i in range(a):
    
    c=input()
    d = list(c)
    check = 0
    for j in d :
        if j == '(':
            check = check + 1
        elif j == ')':
            check = check - 1
        if check == -1 :
            break
    if check == 0 :
        q.append('YES')
    else :
        q.append('NO')
for t in q:
    print(t)