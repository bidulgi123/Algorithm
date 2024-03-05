import sys
input=sys.stdin.readline
dic={}
a,b = map(int,input().split())
for i in range(a):
    c=int(input())
    if c not in dic :
        dic[c]=1
    else :
        dic[c]+=1
for i in dic:
    if dic[i] % b != 0 :
        print(i)
        break