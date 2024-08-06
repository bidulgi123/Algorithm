import sys
input = sys.stdin.readline
def Bellman_Ford(s):
    visit = [987654321] * (a + 1)
    visit[1] = 0
    for i in range(a):
        for j in range(len(graph)):
            st = graph[j][0]
            en = graph[j][1]
            w = graph[j][2]
            if visit[en] > visit[st] + w :
                 visit[en] = visit[st] + w
                 if i == a - 1 : 
                     return True
    return False

for i in range(int(input())):
    a, b, c = map(int, input().split())
    graph = []
    for _ in range(b):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(c):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
    if Bellman_Ford(a) :
        print('YES')
    else :
        print('NO')
