import sys
input=sys.stdin.readline
a, b = map(int,input().split())
cnt=0
cnt2=0
total=[]
for i in range(a):
    c=list(map(str, (input().rstrip())))
    d=set(c)
    if 'X' not in d:
        cnt+=1
    total.append(c)
for j in range(b):
    mid=set()
    for i in range(a):
        mid.add(total[i][j])
    if 'X' not in mid :
        cnt2+=1
print(max(cnt,cnt2))