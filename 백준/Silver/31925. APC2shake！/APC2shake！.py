import sys
input = sys.stdin.readline
dic = {}
for _ in range(int(input().strip())):
    b = input().split()
    if b[1] == 'jaehak' and b[2] == 'notyet':
        if int(b[3]) > 3 or int(b[3]) == -1:
            dic[int(b[4])] = b[0]
total_rank = sorted(dic.keys())[:10]
print(len(total_rank))
print(*sorted([dic[i] for i in total_rank]), sep='\n')
