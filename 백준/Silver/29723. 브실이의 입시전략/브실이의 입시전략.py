import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
subject = {}
for i in range(a):
    name, score = input().rstrip().split()
    subject[name] = int(score)
total = set([input().rstrip() for j in range(c)])
ans = 0
for i in total :
    ans += subject[i]
    del subject[i]
q = sorted(subject.items(), key = lambda x : (x[1], x[0]))
mi, ma = 0, 0
cnt = 0
for i in q :
    if cnt == b - c :
        break
    mi += subject[i[0]]
    cnt += 1
cnt = 0
q = sorted(subject.items(), key = lambda x : (x[1], x[0]), reverse=True)
for i in q :
    if cnt == b - c :
        break
    ma += subject[i[0]]
    cnt += 1
print(ans+mi, ans+ma)