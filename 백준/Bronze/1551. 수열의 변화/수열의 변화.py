a,b=map(int, input().split())
total=list(map(int,input().split(',')))
for j in range(b):
    for i in range(len(total)-1):
        total[i]=total[i+1]-total[i]
    total.pop()
p=[]
for q in total:
    p.append(str(q))
    p.append(',')
p.pop()
for i in p :
    print(i, end='')
    