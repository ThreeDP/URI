n = int(input())
number_in = 0
number_out = 0

for i in range(n):
    value = int(input())
    if value >= 10 and value <= 20:
        number_in += 1
    else:
        number_out += 1

print('{} in\n{} out'.format(number_in,  number_out))

