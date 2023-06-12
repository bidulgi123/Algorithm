import sys
input=sys.stdin.readline
a=int(input())
total=[int(input()) for i in range(a)]
ans=0
for i in range(a):
    if i % 2 != 0 :
        ans-=total[i]
    else :
        ans+=total[i]
result=[]
result.append(ans//2)
total[0]-=(ans//2)
for i in range(1,a):
    total[i] -= total[i-1]
    result.append(total[i-1])
print(*result, sep="\n")