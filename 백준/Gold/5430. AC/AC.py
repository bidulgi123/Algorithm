import sys
from collections import deque

input = sys.stdin.readline

a = int(input().rstrip())
for _ in range(a):
    action = input().rstrip()
    n = input()
    arr_input = input().rstrip()[1:-1].split(',')
    try:
        arr = deque(map(int, arr_input))
    except:
        arr = deque()
    flag = 0
    for i in action:
        if i == 'R':
            flag = 1 - flag  
        elif i == 'D':
            try:
                if flag == 1:
                    arr.pop()
                else:
                    arr.popleft()
            except IndexError:
                print("error")
                break
    else:
        if flag == 1:
            arr.reverse()
        print('[' + ','.join(map(str, arr)) + ']')
