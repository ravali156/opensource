def is_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
n = int(input())
arr = list(map(int,input().split()))
if is_sorted(arr):
    print("true")
else:
    print("false")
