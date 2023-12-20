import sys
input=sys.stdin.readline
a=int(input())
total=[0]
for i in range(a):
    total.append(int(input()))
ans=0
ans_cnt=0
for i in range(1,len(total)):
    visited=[0]*(a+1)
    start=i
    cnt=0
    while True:
        if visited[start] == 1:
            break
        visited[start] = 1
        cnt+=1
        start=total[start]
    if ans < i and ans_cnt < cnt :
        ans_cnt=cnt
        ans=i
print(ans)