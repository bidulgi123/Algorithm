a, b, c = map(int, input().split())
d = set(map(int, input().split()))
e = set(map(int, input().split()))
d, e = d - e, e - d
visit = [1] * (a + 2)
for i in d :
    visit[i] = 0 
for j in e :
    if visit[j - 1] == 0 :
        visit[j - 1] = 1
    elif visit[j + 1] == 0 :
        visit[j + 1] = 1
cnt = 0
for i in range(1, len(visit)-1):
    if visit[i] == 0 : cnt +=1
print(cnt)