y = input("Give year:")
y = int(y)

if y % 4 != 0:
    print(y, "is not a leap year")
else:
    if y % 400 == 0 or y % 100 != 0:
        print(y, "is a leap year")
    else:
        print(y, "is not a leap year")

    







