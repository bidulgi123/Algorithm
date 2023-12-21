for i in range(3):
    a = input()
    b = 1
    cnt = 1
    for j in range(1,len(a)):
        if a[j]==a[j-1]:
            cnt+=1
        else:
            b=max(cnt,b)
            cnt=1
    print(max(cnt, b))