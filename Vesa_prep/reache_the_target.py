def calculate_required_runs(T, test_cases):
    for case in test_cases:
        X, Y = case
        required_runs = X - Y + 1
        print(required_runs)
T = int(input())
test_cases = []
for _ in range(T):
    X, Y = map(int,input().split())
    test_cases.append((X, Y))
calculate_required_runs(T, test_cases)
