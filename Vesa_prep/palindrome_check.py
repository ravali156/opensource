def check_palindrome(S):
    if S == S[::-1]:
        print("TRUE")
    else:
        print("FALSE")
S = input().strip()
check_palindrome(S)
