def dfs(x,y):
    if x<=-1 or x>=b or y>= a or y<=-1 :
        return False 
    if graph[x][y] == 1 :
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x+1,y+1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)
        dfs(x-1,y-1)
        return True
    return False
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    else : 
        graph=[]
        cnt=0
        for i in range(b):
            graph.append(list(map(int, input().split())))
        for j in range(b):
            for i in range(a):
                if dfs(j,i)==True:
                    cnt+=1
    print(cnt)