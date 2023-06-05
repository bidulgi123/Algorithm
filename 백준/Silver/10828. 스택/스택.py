import sys
input=sys.stdin.readline
total=[]
ans=[]
for i in range(int(input())):
    a=input().split()
    if a[0] == 'push' :
        total.append(a[1])
    if a[0] == 'pop' :
        ans.append(total.pop() if total else -1)
    if a[0] == 'size' :
        ans.append(len(total))   
    if a[0] == 'empty' :
        ans.append(0 if len(total) != 0 else 1)
    if a[0] == 'top' :
        ans.append(total[-1] if total else -1)

for i in ans:
    print(i)