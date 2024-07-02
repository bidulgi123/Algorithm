import sys
input = sys.stdin.readline
dic = {}
for i in range(int(input())):
    a, b = map(str, input().split())
    if a in dic :
        dic[a] += int(b) 
    else :
        dic[a] = int(b)
for i in dic :
    if dic[i] == 5 :
        print('YES')
        sys.exit()
print('NO')