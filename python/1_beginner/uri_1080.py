lista = []
for i in range(0,100):
    lista.append(int(input()))

print("{}\n{}".format(max(lista), lista.index(max(lista)) + 1))