input()
total=set(list(input().split()))
ans=0
for i in total:
    if i[-6:] == 'Cheese':
        ans+=1
if ans >= 4 :
    print('yummy')
else :
    print('sad')