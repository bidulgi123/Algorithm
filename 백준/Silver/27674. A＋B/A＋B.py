for i in range(int(input())):
    input()
    a=input()
    a=list(str(a))
    a = sorted(list(map(lambda x: int(x), a)),reverse=True)
    print(int(''.join(map(str, a[:-1])))+int(a[-1]))