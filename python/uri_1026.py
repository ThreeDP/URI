def dec_bin(n): #Converte de decimal para binario.
    b = []
    while n != 0:
        b.append(int(n % 2))
        n = int(n / 2)
    while len(b) < 32:
        b.append(int(0))
    return b[::-1] # Inverte a string.

def bin_dec(binar): #Converte de binario para decimal.
    base = 2 ** (len(binar) - 1) #Traz o tamanho da lista e -1 para descontar a posição 01 da base binaria.
    result = 0
    for n in binar:
        result += base * n
        base = int(base / 2)
    return result

def calc(number): #Realiza o calculo lógico necessario.
    result = []
    A = dec_bin(number[0])
    B = dec_bin(number[1])
    for n in range(len(A)):
        if A[n] != 1 and B[n] == 1 or A[n] == 1 and B[n] != 1:
            result.append(1)
        else:
            result.append(0)
    R = bin_dec(result)
    return R

if __name__ == "__main__":
    while True:
        try:
            number_A = [int(x) for x in input().split(" ")]
            number_B = [int(y) for y in input().split(" ")]
        except EOFError:
            break

    print("{}\n{}".format(calc(number_A), calc(number_B)))