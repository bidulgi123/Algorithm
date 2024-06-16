import sys
a = int(input())
b = list(map(int, input().split()))
t = []
cnt = 1
for i in b :
    t.append(i)
    while t and t[-1] == cnt:
        t.pop()
        cnt+=1
if t :
    print("Sad")
else :
    print("Nice")