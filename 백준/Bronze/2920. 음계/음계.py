total=list(map(int, input().split()))
if total == sorted(total):
    print('ascending')
elif total == sorted(total,reverse=True):
    print("descending")
else :
    print("mixed")