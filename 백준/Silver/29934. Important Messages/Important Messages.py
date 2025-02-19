from collections import Counter
import sys
input = sys.stdin.readline
f = set(input() for _ in range(int(input()))) 
s = [input() for _ in range(int(input()))]  
ans = sum(Counter(s)[i] for i in f)  
print(ans)