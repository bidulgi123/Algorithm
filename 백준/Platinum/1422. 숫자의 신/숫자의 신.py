import sys
input=sys.stdin.readline
a,b=map(int,input().split())
total=[]
for i in range(a):
  total.append(int(input()))
for j in range(b-a):
  total.append(max(total))
def find(total):
    sorted_list = sorted(map(str, total), reverse=True, key=lambda x: x*(len(max(map(str, total), key=len))+1))
    largest = ''.join(sorted_list)
    print(largest)
find(total)