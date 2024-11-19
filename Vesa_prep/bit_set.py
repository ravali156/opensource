N, k = map(int, input().strip())
if N & (1 << k):
    print("true")
else:
    print("false")
