coins = int(input())
coins_values = []

while True:
    try: # Add valores moedas
        for i in range(0, coins, 1): 
            coins_values.append(int(input()))
        jump_number = int(input())
    except Exception:
        pass

    result_number = 0
    # Soma de acordo com salto.
    check = coins - 1
    print(check, coins_values)
    while check >= 0:
        result_number += coins_values[check]
        check -= jump_number
        print(check)

    print(result_number)        

    cont = 0
    for j in range(result_number):
        if result_number % (j + 1) == 0:
            cont += 1

    if cont == 2:
        print("You're a coastal aircraft, Robbie, a large silver aircraft.")
        break
    else:
        print("Bad boy! I'll hit you")
        coins_values.clear()
