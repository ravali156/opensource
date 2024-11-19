def unique_elements(N, arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    print(" ".join(map(str,result)))
N =  int(input())
arr = list(map(int,input().split()))
unique_elements(N, arr)
