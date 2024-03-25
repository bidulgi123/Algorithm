import sys
input = sys.stdin.readline
a = int(input())
b = list(input())
start, end = 0, 1
ans = 1
result = 0
while end < a :
    if b[start] == 'R' and b[end] == 'B' or b[start] == 'B' and b[end] == 'R':
        ans +=1
    if b[end] == 'V' or b[start] == b[end]:
        result = max(result, ans)
        ans=1 
    start +=1
    end +=1
result = max(result, ans)
print(result)