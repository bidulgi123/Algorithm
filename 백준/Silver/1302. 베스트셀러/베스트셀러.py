import sys
input = sys.stdin.readline
book={}
for i in range(int(input())):
    a=input().rstrip()
    if a in book :
        book[a] +=1
    else :
        book[a] = 1
sorted_dict = list(sorted(book.items(),  key=lambda item: (-item[1], item[0])))
print(sorted_dict[0][0])
