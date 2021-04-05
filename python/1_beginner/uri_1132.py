sum_numbers = 0
x = int(input())
y = int(input())

if y < x:
    z = x
    x = y
    y = z

while x <= y:
    if x % 13 != 0:
        sum_numbers += x
    x += 1

print(sum_numbers)