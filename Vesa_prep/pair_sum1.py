def find_pair_with_sum(arr, k):
    seen = set()
    for num in arr:
        complement = k - num
        if complement in seen:
            return "true"
        seen.add(num)
    return "false"
N = int(input())
arr = list(map(int, input().split()))
K = int(input())
print(find_pair_with_sum(arr, K))
