leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

for n in range(0, int(input()), 1):
    numbers = input()
    result = 0
    for number in numbers:
        result += leds[number]
    
    print("{} leds".format(result))

