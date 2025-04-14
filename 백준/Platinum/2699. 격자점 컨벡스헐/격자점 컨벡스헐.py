import sys
import math
input = sys.stdin.readline

def angle_from_first(p):       
    return math.atan2(p[1] - first_point[1], p[0] - first_point[0])

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(points)
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

for _ in range(int(input())):
    a = int(input())
    if a % 5 != 0 :
        a = a // 5 + 1
    else : 
        a = a // 5 

    points = []
    for __ in range(a):
        point = list(map(int, input().split()))
        points += [point[i:i+2] for i in range(0, len(point), 2)]
    t = convex_hull(points)
    first_point = sorted(t, key=lambda x: (x[1],x[0]), reverse=True)[0]
    sorted_points = sorted(t, key=angle_from_first, reverse=True)
    print(len(t))
    for item in sorted_points :
        print(*item)