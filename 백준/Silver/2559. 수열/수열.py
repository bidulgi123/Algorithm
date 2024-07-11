a, b = map(int,input().split())
total = list(map(int,input().split()))
prefix_sum = []
prefix_sum.append(sum(total[:b]))
for i in range(a-b):
    prefix_sum.append(prefix_sum[i]-total[i]+total[b+i])
print(max(prefix_sum))