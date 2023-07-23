a = input()
total = [0]*26
for i in a:
    total[ord(i)-97] += 1  
for j in total:
    print(j, end=' ')