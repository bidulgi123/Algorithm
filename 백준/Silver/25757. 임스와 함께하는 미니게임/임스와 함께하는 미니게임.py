import sys
input = sys.stdin.readline
a, b = input().rstrip().split()
total = set()
for i in range(int(a)):
    total.add(input().rstrip())
if b == 'Y' :
    print(len(total))
elif b == 'F' :
    print(len(total)//2)
else :
    print(len(total)//3)
