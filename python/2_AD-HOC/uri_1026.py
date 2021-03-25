while True:
    try:
        x, y = [int(i) for i in input().split()]
        r = x ^ y
        print(r)
    except EOFError:
        break