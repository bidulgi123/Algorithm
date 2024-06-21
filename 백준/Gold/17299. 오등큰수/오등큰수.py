import sys
a = int(input())
b = list(map(int, input().split()))
check = [0] * 1000001
t = []
ans = [-1] * a
for i in b :
    check[i] +=1 
for i in range(a):
    while t and check[b[t[-1]]] < check[b[i]]:
        ans[t.pop()] = b[i]
    t.append(i)
print(*ans)