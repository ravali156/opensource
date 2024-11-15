def can_achieve_marks(N, X, Y):
    if Y % X == 0:
        k = Y // X
        if 0 <= k <= N:
            return "YES"
    return "NO"
N, X, Y = map(int, input().split())
print(can_achieve_marks(N, X, Y))
