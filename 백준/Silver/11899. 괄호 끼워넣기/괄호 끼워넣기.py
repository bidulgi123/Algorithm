import sys
from collections import deque
import copy
a=deque(input())
w=copy.deepcopy(a)
middle=deque()
cnt=0
for i in range(len(a)):
    b=a.popleft()
    try :
        if b == ')' and middle[-1] == '(':
            cnt+=2
            middle.pop()
        else :
            middle.append(b)
    except :
        middle.append(b)
print(len(w)-cnt)

