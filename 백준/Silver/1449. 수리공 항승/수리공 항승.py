import sys
input = sys.stdin.readline
a, b = map(int,input().split())
total=list(map(int,input().split()))
total.sort()
start = total[0]
ans = 1
for i in range(1,a):
    if total[i] >= start+b : 
        ans+=1
        start=total[i]
print(ans)