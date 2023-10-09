import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int,input().split()))
if a == 1 :
    print(0)
    sys.quit()
total=[0]
cnt=0
for i in range(1,a):
    if b[i-1] < b[i] :
        cnt +=  b[i]-b[i-1]
    else :
        total.append(cnt)
        cnt=0
total.append(cnt)
print(max(total))

