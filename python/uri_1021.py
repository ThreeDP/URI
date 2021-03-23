monetar = float(input())
banknotes = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
bank = []
p_mood = 'nota'
for note in banknotes:
    bank.append(int(monetar / note))
    monetar = monetar - bank[banknotes.index(note)] * note

i = 0
for n in bank:
    if banknotes[i] == 100:
        print("NOTAS:")
    if banknotes[i] == 1:
        print("MOEDAS:")
        p_mood = 'moeda'
    print("{qtd} {p_mood}(s) de R$ {cash:.2f}".format(qtd = n, p_mood = p_mood, cash = banknotes[i]))
    i += 1

