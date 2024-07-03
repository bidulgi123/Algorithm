import sys
input = sys.stdin.readline
a = int(input())
start = {}
end = []
for i in range(a):
    start[input()] = i
for i in range(a, 0, -1):
    end.append(input())
cnt = 0 
for i in range(a-1):
	for j in range(i+1, a):
		if start[end[i]] > start[end[j]]:
			cnt += 1
			break
print(cnt)