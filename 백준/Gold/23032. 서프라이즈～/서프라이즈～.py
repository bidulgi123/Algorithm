import itertools
a = int(input())
b = list(map(int, input().split()))
prefix_sum = [0] + list(itertools.accumulate(b))
min_diff = float('inf')
max_sum = 0
for start in range(a):
    for end in range(start + 1, a + 1):
        total_sum = prefix_sum[end] - prefix_sum[start]  
        left_sum = 0
        mid = start + 1  
        while mid < end:
            left_sum = prefix_sum[mid] - prefix_sum[start]
            right_sum = total_sum - left_sum
            diff = abs(left_sum - right_sum)
            if diff < min_diff or (diff == min_diff and total_sum > max_sum):
                min_diff = diff
                max_sum = total_sum
            if left_sum < right_sum:
                mid += 1  
            else:
                break  
print(max_sum)