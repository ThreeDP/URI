def fat(i):
    if i <= 1:
        return 1
    else:
        return fat(i - 1) * i

n = int(input())
print(fat(n))
