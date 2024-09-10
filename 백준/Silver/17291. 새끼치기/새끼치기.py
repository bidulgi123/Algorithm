a = int(input())
b = [0, 1, 2, 4, 7]
for i in range(5, 21):
    if i % 2 == 0:
        b.append(b[i - 1] * 2 - b[i - 4] - b[i - 5])
    else :
        b.append(b[i - 1] * 2)
print(b[a])