a = int(input())
b = list(map(int, input().split()))
print(len(b)-len(set(b)))