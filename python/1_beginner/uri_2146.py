numbers = []

while True:
    try:
        numbers.append(int(input()) - 1)
    except Exception:
        break

for n in numbers:
    print(n)

