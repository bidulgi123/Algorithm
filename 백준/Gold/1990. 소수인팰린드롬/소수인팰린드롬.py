a, b = map(int, input().split())
def Eratos(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    return True
for i in range(a, 10000001):
    if i > b : 
        break
    if str(i) == str(i)[::-1] :
        if Eratos(i) :
            print(i)
print(-1)   