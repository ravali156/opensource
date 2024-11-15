month = int(input().strip())
if 1 <= month <= 12:
    if 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
