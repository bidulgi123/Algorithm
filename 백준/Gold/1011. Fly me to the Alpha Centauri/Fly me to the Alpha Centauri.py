for i in range(int(input())) :
    x,y = map(int,input().split())
    dis = y - x
    cnt=1
    while True :
        if cnt**2 <= dis < (cnt+1)**2 :
            break
        else:
            cnt += 1
    if cnt**2 == dis :
        print((cnt*2)-1)
    elif cnt**2 < dis <= cnt**2 + cnt :
        print(cnt*2)
    else :
        print((cnt*2)+1)