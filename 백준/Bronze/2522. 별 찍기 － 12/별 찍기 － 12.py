import sys 
input = sys.stdin.readline
l = int(input())
cnt = l - 1
for i in range(1 ,l):
    print(' '*cnt+'*'*i)
    cnt -= 1
print('*'*l)
cnt = l - 1
for j in range(1, l):
    print(' '*j+'*'*cnt)
    cnt -= 1
