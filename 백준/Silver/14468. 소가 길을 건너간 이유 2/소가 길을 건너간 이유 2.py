import sys
from collections import Counter
input=sys.stdin.readline
a=input().rstrip()
cnt=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            total=Counter(a[i:j+1])
            for _ in total:
                if total[_]==1:
                    cnt+=1
print(cnt//2)
            