values = [int(x) for x in input().split(" ")]
result = 0
stop = values[-1]
for i in range(0, stop, 1):
    result += values[0] + i

print(result)
