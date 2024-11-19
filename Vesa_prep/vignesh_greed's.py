def largest_perimeter_triangle(n, sticks):
    sticks.sort(reverse=True)
    for i in range(n - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            return sticks[i] +sticks[i + 1] + sticks[i + 2]
    return -1
n = int(input())
sticks = list(map(int, input().split()))
print(largest_perimeter_triangle(n, sticks))
