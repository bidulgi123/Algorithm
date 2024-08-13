import sys
input = lambda: sys.stdin.readline().rstrip()
a,b=map(int,input().split())
total_a=set([input() for i in range(a)])
total_b=set([input() for i in range(b)])
ans=list(total_a & total_b)
ans=list(total_a & total_b)
print(len(ans))
print(*sorted(ans), sep='\n')