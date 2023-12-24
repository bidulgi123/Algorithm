a=input()
middle=1
total='z'*52
for i in range(middle,len(a)):
    for j in range(i+1,len(a)):
        middle=a[:i][::-1]+a[i:j][::-1]+a[j:][::-1]
        if middle<total:
            total=middle
print(total)  