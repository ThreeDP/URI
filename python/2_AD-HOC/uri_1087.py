x1, y1, x2, y2 = [int(x) for x in input().split(" ")]

while (x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0):
    result = 0
    while True:
        if x1 == x2 and y1 == y2:
            result = 0;
            break
        elif (x2 + y2) == (x1 + y1):
            result += 1
            break
        elif (x1 - x2) == (y1 - y2):
            result += 1
            break
        elif (x1 == x2) and (y1 > y2 or y1 < y2):
            result += 1
            break
        elif (y1 == y2) and (x1 > x2 or x1 < x2):
            result += 1
            break
        else:
            result += 1
            x1 += (x2 - x1)
            continue
    print(result)
    x1, y1, x2, y2 = [int(x) for x in input().split(" ")]
    
