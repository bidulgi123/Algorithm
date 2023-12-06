import sys
input=sys.stdin.readline
for i in range(int(input())):
    se=list(input().split())
    animal=set()
    while True:
        sentence=input().rstrip()
        if sentence == 'what does the fox say?':
            break
        else :
            t=list(sentence.split())
            animal.add(t[-1])
    for i in se:
        if i in animal:
            continue
        else :
            print(i, end=' ')