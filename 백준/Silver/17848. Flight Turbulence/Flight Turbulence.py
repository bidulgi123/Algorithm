a, b = map(int,input().split())
total = list(map(int, input().split()))
ans=0
move=b
while True:
    if total[move-1] == b :
        break
    else :
        ans+=1
        move=total[move-1]
if ans == 0:
    print(0)
else :
    print(ans+1)