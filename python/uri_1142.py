N = int(input())
count = 1
pum = "PUM"

for n in range(N):
    print("{} {} {} {}".format(count, count + 1, count + 2, pum))
    count += 4