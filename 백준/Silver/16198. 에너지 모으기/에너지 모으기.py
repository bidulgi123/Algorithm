import sys
input = sys.stdin.readline
a = int(input())
total = list(map(int, input().split()))
ans = 0
def tr(s):
    global ans
    if len(total) == 2 :
        ans = max(s, ans)
        return
    for i in range(1,len(total)-1):
        p = total[i-1] * total[i+1]
        q = total.pop(i)
        tr(s + p)
        total.insert(i, q)
tr(0)
print(ans)