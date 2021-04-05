triangle = [float(x) for x in input().split()]

i = triangle.index(max(triangle))
resto = [float(y) for y in triangle] 
resto[i:i+1] = [] #Retirar o maior lado da lista

if triangle[i] < sum(resto): #Verifica se o maior lado é menor que a soma dos demais.
    print("Perimetro = {:.1f}".format(sum(triangle)))

else:
    A = ((triangle[0] + triangle[1]) / 2) * triangle[2]
    print("Area = {:.1f}".format(A))
