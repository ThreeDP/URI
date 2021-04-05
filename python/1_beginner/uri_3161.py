N, M = [int(x) for x in input().split(" ")]
frutas = []
lista = []

checker = 0
for n in range(N):
    frutas.append(input())
for n in range(M):
    lista.append(input())

for eat in frutas:
    i = 1
    for fruta in lista:
        if fruta.lower().find(eat.lower()) != -1 or fruta.lower().find(eat[::-1].lower()) != -1:
            print("Sheldon come a fruta {}".format(eat.lower()))
            break
        elif i == M:
            print("Sheldon detesta a fruta {}".format(eat.lower()))
        i += 1
