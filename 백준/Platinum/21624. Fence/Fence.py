import sys
import math
input = sys.stdin.readline

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def angle_from_first(p):       
    return math.atan2(p[1] - first_point[1], p[0] - first_point[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]  

n, l = map(int, input().split())
total = [list(map(int, input().split())) for _ in range(n)]
move = [(l, 0), (-l, 0), (0, l), (0, -l)]
new_total = []
for y, x in total :
    for my, mx in move :
        dy = my + y
        dx = mx + x 
        new_total.append((dy, dx))

t = convex_hull(new_total)
first_point = sorted(t, key=lambda x: (x[1],x[0]), reverse=True)[0]
sorted_points = sorted(t, key=angle_from_first, reverse=True)
ans = 0
for idx, pt in enumerate(sorted_points):
    town = math.sqrt((sorted_points[idx-1][0] - sorted_points[idx][0])**2+(sorted_points[idx-1][1] - sorted_points[idx][1])**2)
    ans += town
print(ans)