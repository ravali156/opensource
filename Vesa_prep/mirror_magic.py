def generate_mirror_image(N, matrix):
    for row in matrix:
        print(" ".join(map(str,row[::-1])))
N = int(input())
matrix = []
for _ in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)
generate_mirror_image(N, matrix)
