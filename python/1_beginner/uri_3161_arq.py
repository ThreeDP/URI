def find_end(Ofile):
    lista = open(Ofile)
    count = 0
    for lines in lista:
        count += 1
    return count

if __name__ == "__main__":
    N = int(input("Entre o numero de frutas...:  "))
    Ofile = input("Entre o nome do arquivo....:  ")
    frutas = []

    lines = find_end(Ofile)

    for n in range(N):
        frutas.append(input())

    for eat in frutas:
        lista = open(Ofile)
        i = 1
        for fruta in lista:
            if fruta.lower().find(eat.lower()) != -1 or fruta.lower().find(eat[::-1].lower()) != -1:
                print("Sheldon come a fruta {}".format(eat.lower()))
                break
            elif i == lines:
                print("Sheldon detesta a fruta {}".format(eat.lower()))
            i += 1
        lista.close()

