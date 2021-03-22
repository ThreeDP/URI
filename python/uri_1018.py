result = []
banknotes = [100, 50, 20, 10, 5, 2, 1]
N = int(input())
manip = N
for x in banknotes:
    result.append(int(manip / x))
    manip = manip - result[banknotes.index(x)] * x

i = 0
print("{}".format(N))
for r in result:
    print("{notes} nota(s) de R$ {value_n},00".format(notes = r, value_n = banknotes[i]))
    i+=1







