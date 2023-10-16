import sys
input = sys.stdin.readline
file={}
a=int(input())
for i in range(a):
    b=list(map(str,input().rstrip().split('.')))
    if b[1] not in file :
        file[b[1]]=1
    else :
        file[b[1]]+=1
sorted_dict = list(sorted(file.items(),  key=lambda item: (item[0])))
for name, num in sorted_dict :
    print(name, num)