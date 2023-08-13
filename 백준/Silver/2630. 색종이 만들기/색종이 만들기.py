import sys
input=sys.stdin.readline
a=int(input())
total=[list(map(int,input().split())) for i in range(a)]
b=0
w=0
def divide(i,j,p):
    global b,w
    now = total[i][j] 
    for q in range(i, i+p):
        for t in range(j, j+p):
            if now != total[q][t]:
                divide(i,j,p//2)
                divide(i,j+p//2,p//2)
                divide(i+p//2,j,p//2)
                divide(i+p//2,j+p//2,p//2)
                return
    if now == 0:
        w += 1
    else:
        b += 1
divide(0,0,a)
print(w)
print(b)