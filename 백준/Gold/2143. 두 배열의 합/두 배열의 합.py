from bisect import bisect_left, bisect_right
import sys
input=sys.stdin.readline
a=int(input())
b=int(input())
first = list(map(int, input().split()))
c=int(input())
end = list(map(int, input().split()))
first_total=[]
end_total=[]
for i in range(b):
    q=0
    for t in range(i,b):
        q+=first[t]
        first_total.append(q)
for i in range(c):
    q=0
    for t in range(i,c):
        q+=end[t]
        end_total.append(q)
end_total.sort()
ans=0
for i in first_total:
    ans+=(bisect_right(end_total,a-i)-bisect_left(end_total,a-i))
print(ans)