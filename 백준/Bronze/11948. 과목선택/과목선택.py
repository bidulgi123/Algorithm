import sys
input=sys.stdin.readline
total_a=[]
total_b=[]
for i in range(4):
    total_a.append(int(input()))
for j in range(2):
    total_b.append(int(input()))
total_a.sort(reverse=True)
total_b.sort(reverse=True)
print(sum(total_a[:3])+total_b[0])
    