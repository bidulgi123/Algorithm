import sys
input = sys.stdin.readline
st = []
for i in range(int(input())) :
    a = list(map(int, input().split()))
    if a[0] == 1 :
        st.append(a[1])
    if a[0] == 2 :
        if st : 
            print(st.pop())
        else :
            print(-1)
    if a[0] == 3 :
        print(len(st))
    if a[0] == 4 :
        if len(st) == 0 :
            print(1)
        else :
            print(0)
    if a[0] == 5 :
        if st :
            print(st[-1])
        else :
            print(-1)