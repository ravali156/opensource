def check_frequency(T, frequencies):
    for X in frequencies:
        if 67 <= X <= 45000:
            print("YES")
        else:
            print("NO")
T = int(input())
frequencies = []
for _ in range(T):
    X = int(input())
    frequencies.append(X)
check_frequency(T, frequencies)
