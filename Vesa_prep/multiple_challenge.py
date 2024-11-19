def count_divisible_by_3_or_5(N):
    count_3 = N // 3
    count_5 = N // 5
    count_15 = N // 15
    count = count_3 + count_5 - count_15
    return count
N = int(input())
print(count_divisible_by_3_or_5(N))
