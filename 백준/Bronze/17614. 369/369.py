a=int(input())
cnt=0
for j in range(1,a+1):
    for i in str(j):
        if '3' == i or '6' == i or '9' == i:
            cnt+=1
print(cnt)