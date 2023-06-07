import sys
input=sys.stdin.readline
total=[int(input()) for i in range(int(input()))]
total.sort()
def round(a):
    if a - int(a) >= 0.5 :
        return int(a) + 1
    else :
        return int(a)
start=round(len(total)*0.15)
ans=total[start:len(total)-start]
if len(ans) != 0 :
    print(round((sum(ans)/len(ans))))
else:
    print(0)