for i in range(0, int(input()), 1):
    n = int(input())
    if n > 0:
        if n % 2 == 0:
            print("EVEN POSITIVE")
        elif n % 2 != 0:
            print("ODD POSITIVE")
    elif n < 0:
        if n % 2 == 0:
            print("EVEN NEGATIVE")
        elif n % 2 != 0:
            print("ODD NEGATIVE")
    else:
        print("NULL")