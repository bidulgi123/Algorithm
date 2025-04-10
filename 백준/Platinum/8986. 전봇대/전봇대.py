a = int(input())
b = list(map(int, input().split()))

def prefix_sum(x):
    return sum(abs(x * i - b[i]) for i in range(a))

left = 0
right = 1000000000
mid_sum = 0

while True :
    left_third = left + (right - left) // 3 
    right_third = right - (right - left) // 3 
    if right - left < 3 :
        break
    
    if prefix_sum(left_third) > prefix_sum(right_third) :
        left = left_third
    else :
        right = right_third

ans = float('inf')
for i in range(left, right+1):
    ans = min(ans, prefix_sum(i))
    
print(ans)