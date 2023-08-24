import math
import sys
for i in range(int(input())):
    input=sys.stdin.readline
    a,b = map(int, input().split())
    print(math.lcm(a,b))