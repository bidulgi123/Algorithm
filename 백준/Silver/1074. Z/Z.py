import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
def Z(a,b,c):
    if a == 0:
        return 0
    return 2*(b%2)+(c%2)+4*Z(a-1,b//2,c//2)
a,b,c= map(int, input().split())
print(Z(a,b,c))