def find_max_consecutive_absent_days(N, attendance_record):
    max_absent = 0
    current_absent = 0
    for day in attendance_record:
        if day == '0':
            current_absent += 1
        else:
            max_absent = max(max_absent, current_absent)
            current_absent = 0
    max_absent = max(max_absent, current_absent)
    return max_absent
N = int(input())
attendance_record = input().strip()
print(find_max_consecutive_absent_days(N, attendance_record))
