for n in range(0, int(input()), 1):
    
    x, y = [int(x) for x in input().split(" ")]
    sum = 0

    if x > y:
        sing = -1
    else:
        sing = 1
    x += sing

    for i in range(x, y, sing):
        if (i) % 2 != 0:
            sum += i
    
    print(sum)