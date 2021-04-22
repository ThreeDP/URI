M = int(input())
v = []
primos = []
dividers = False

while True:
    try:
        for i in range(0, M, 1):
            v.append(int(input()))
    except EOFError:
        break
        
    result = 0
    n = int(input())

    for i in range(0, len(v), n):
        result += v[-(i + 1)]

    r = 1

    while r <= result:
        primos.append(r)
        r += 1

    for p in primos:
        for x in range(2, result + 1):
            lr = p * x
            if p == result:
                dividers = True
            elif p == 1 or lr > result:
                break
            try: 
                ip = primos.index(lr)
                del(primos[ip])
                #print(primos)
            except:
                continue
        if p == 11 and primos[-1] == result:
            dividers = True
            break
        elif p == 11:
            break

    if dividers == True:
        print("You're a coastal aircraft, Robbie, a large silver aircraft.")
        continue
    else:
        print("Bad boy! I'll hit you")
        v.clear()
        primos.clear()