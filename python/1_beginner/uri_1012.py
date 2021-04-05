pi = 3.14159
# Faz a entrada de uma linha de dados e converte os dados para float.

A, B, C = [float(x) for x in input().split(" ")]

triangle = (A * C) / 2
circle = pi * C ** 2
trapez = ((A + B) / 2) * C
square = B * B
rectan = A * B

print("TRIANGULO: {:.3f}".format(triangle))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trapez))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rectan))
