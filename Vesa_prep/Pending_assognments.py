X, Y, Z = map(int,input().split())
total_time_needed = X * Y
total_time_available = 2 * 24 * 60
if total_time_needed <= total_time_available:
    print("YES")
else:
    print("NO")
