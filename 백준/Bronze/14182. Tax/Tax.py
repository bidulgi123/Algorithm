while True:
    a = int(input())
    if a == 0 :
        break
    if a <= 1000000 :
        print(a)
    elif 1000000 < a <= 5000000:
        print(int(a-a*0.1))
    else :
        print(int(a-a*0.2))