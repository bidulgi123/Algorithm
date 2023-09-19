import sys
sys.setrecursionlimit(10**9)
# input=sys.stdin.readline
a=list(input())
b=list(input())
flag=0
def find(noun):
  global flag
  if noun == a :
    flag=1
    return 1
  if len(noun)==0:
    return 0
  if noun[-1]=='A' :
    find(noun[:-1])
  if noun[-1]=='B':
    find(noun[:-1][::-1])
find(b)
print(flag)