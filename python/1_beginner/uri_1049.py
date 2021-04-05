animal = {'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba' }, 'mamifero':{'onivoro': 'homem', 'herbivoro': 'vaca'}}, 'invertebrado':{'inseto':{'hematofago': 'pulga', 'herbivoro': 'lagarta'}, 'anelideo': { 'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}}

n1 = input()
n2 = input()
n3 = input()

print(animal[n1][n2][n3])