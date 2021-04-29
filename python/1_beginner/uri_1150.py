x = int(input())
while True:
    z = int(input())
    if z > x:
        break

result = 1
while True:
    result += 1
    if x > z:
        break
    x += (x + result)

print(result)

