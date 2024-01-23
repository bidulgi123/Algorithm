import sys
import math
input=sys.stdin.readline
for i in range(int(input())):
    a,b=map(int,input().split())
    print(math.lcm(a,b),math.gcd(a,b))