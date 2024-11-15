def students_without_tickets(T, test_cases):
    for i in range(T):
        N, M = test_cases[i]
        print(max(0, N - M))
T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    test_cases.append((N, M))
students_without_tickets(T, test_cases)
