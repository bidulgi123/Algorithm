import sys
input=sys.stdin.readline
total=[input().rstrip() for i in range(int(input()))]
for i in range(len(total)):
    q=0
    for j in total[i]:
         if j.isdigit():
            q += int(j)
    total[i]=(total[i],q)
total.sort(key=lambda x:(len(x[0]),x[1],x[0]))
for i in total:
    print(i[0])