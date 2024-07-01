import bisect
a, b, c = map(int, input().split())
t = list(map(int, input().split()))
chul = list(map(int, input().split()))
t.sort()
visited = [0] * b
for i in chul :
    mid = bisect.bisect_right(t, i)
    while True :
        if visited[mid] == 0 :
            visited[mid] = 1 
            print(t[mid])
            break
        else :
            mid += 1