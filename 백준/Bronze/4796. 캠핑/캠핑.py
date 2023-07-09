import sys
input=sys.stdin.readline
cnt=0
while True:
    a,b,c=map(int,input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    total=0
    total+=((c//b)*a)
    total+=min(c%b,a)
    cnt+=1
    print(f"Case {cnt}: {total}")