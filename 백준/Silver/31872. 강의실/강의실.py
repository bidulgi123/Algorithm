a, b = map(int, input().split())
t = list(map(int, input().split()))
t.append(0)
t.sort()
q = []
for i in range(1, a + 1):
    q.append(t[i] - t[i - 1])
q.sort(reverse=True)
print(sum(q[b:]))