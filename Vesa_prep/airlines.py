import math
x, N = map(int, input().split())
planes_needed = (N + 99) // 100
new_planes_needed = max(0, planes_needed - x)
print(new_planes_needed)
