a = int(input())
b = list(map(int, input().split()))
cnt = 1
for i in range(1,a):
    if b[i-1] <= b[i]:
        cnt+=1
print(cnt)