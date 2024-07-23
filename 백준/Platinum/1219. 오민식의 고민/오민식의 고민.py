import sys
input = sys.stdin.readline
a, s, e, d = map(int, input().split())
city = [-float("inf")] * a 
graph = [list(map(int,input().split())) for _ in range(d)]
bias = list(map(int, input().split()))
def bellman_ford(start):
    city[start] = bias[start]
    for i in range(a + 100000) :
        for j in range(d) : 
            st = graph[j][0]
            en = graph[j][1]
            value = graph[j][2]
            if city[st] != -float("inf") and city[en] < city[st] - value + bias[en] :
                city[en] =  city[st] - value + bias[en]
                if i > a :
                    city[en] = float("inf")
    if city[e] == -float('inf'):
        print('gg')
    elif city[e] == float('inf') :
        print('Gee') 
    else :
        print(city[e])
bellman_ford(s)