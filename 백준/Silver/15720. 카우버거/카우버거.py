import sys
input=sys.stdin.readline
input()
burger=sorted(list(map(int,input().split())),reverse=True)
side=sorted(list(map(int,input().split())),reverse=True)
drink=sorted(list(map(int,input().split())),reverse=True)
total=0
q=min(len(burger),len(drink),len(side))
for i in range(q):
    total+=(burger[i]+side[i]+drink[i])*0.9
total+=sum(burger[q:])
total+=sum(side[q:])
total+=sum(drink[q:])
print(sum(burger+side+drink))
print(int(total))