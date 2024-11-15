def reverse_array(n, arr):
    reversed_arr= arr[::-1]
    print(" ".join(map(str,reversed_arr)))
n = int(input())
arr = list(map(int, input().split()))
reverse_array(n, arr)
