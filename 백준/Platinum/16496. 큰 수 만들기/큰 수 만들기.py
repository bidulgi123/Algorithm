import sys
input=sys.stdin.readline
a=int(input())
b=list(map(int, input().split()))
def find(total):
    sorted_list = sorted(map(str, total), reverse=True, key=lambda x: x*(len(max(map(str, total)))+1))
    largest = ''.join(sorted_list)
    print(int(largest))
find(b)