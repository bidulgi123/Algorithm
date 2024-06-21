import sys
input = sys.stdin.readline
c = 0
while True : 
    c += 1 
    a = input().rstrip()
    check = []
    if '-' in a :
        break
    cnt = 0
    for i in a :
        if not check and i == '}':
            check.append('{')
            cnt +=1
        elif check and i == '}':
            check.pop()
        else :
            check.append(i)
    cnt += len(check) // 2 
    print(str(c)+'.', cnt)