import sys
input = sys.stdin.readline
a = int(input())
cow = list(map(int, input().split()))

def ice_age(time):
    max_ans = -float('inf')
    for i in range(a):
        max_ans = max(abs(time - i) * cow[i], max_ans)
    return max_ans

left = 0
right = a

while right - left > 2 :
    left_third = left + (right - left) // 3 
    right_third = right - (right - left) // 3 

    if ice_age(left_third) > ice_age(right_third) :
        left = left_third

    else :
        right = right_third

ans = float('inf')
for t in range(left, right + 1):
    ans = min(ans, ice_age(t))
    
print(ans)