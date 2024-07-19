import sys
input = sys.stdin.readline
for i in range(int(input())):
    input()
    a = list(map(int, input().split()))
    a = set(a)
    input()
    c = list(map(int, input().split()))
    for i in c :
        if i in a :
            print(1)
        else : 
            print(0)