import sys
input=sys.stdin.readline
input()
a=set(list(map(int,input().split())))
b=int(input())
if b in a : 
  print(0)
else :
  sort_a = sorted(a)
  cnt=0
  min_a=0
  for i in sort_a:
    if i < b :
      min_a=i
    elif i > b:
      max_a=i
      break
  for i in range(min_a+1,max_a-1):
    for j in range(i+1,max_a):
      if i <= b and j >= b:
        cnt+=1
  print(cnt)