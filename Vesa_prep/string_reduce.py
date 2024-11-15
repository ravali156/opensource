def reduce_string(s):
    result = []
    if not s:
        return ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)
input_string = input().strip()
print(reduce_string(input_string))
