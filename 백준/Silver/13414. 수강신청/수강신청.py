import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total={}
for i in range(b):
    total[input()]=i
ans=sorted(total.items(), key = lambda x:x[1])
cnt = 0
for i in ans:
    if cnt == a:
        break
    print(i[0], end='')
    cnt += 1