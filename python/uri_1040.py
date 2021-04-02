n1, n2, n3, n4 = [float(x) for x in input().split(" ")]
average = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

print("Media: {:.1f}".format(average))

if average >= 7:
    print("Aluno aprovado.")

elif average < 7 and average >= 5:
    print("Aluno em exame.")
    exame = float(input())
    
    print("Nota do exame: {:.1f}".format(exame))
    ex_average = (exame + average) / 2
    
    if ex_average >= 5 and ex_average < 10:
        print("Aluno aprovado.")
    elif ex_average < 5 and ex_average >= 0:
        print("Aluno reprovado.")
    
    print("Media final: {:.1f}".format(ex_average))

elif average < 5 and average >= 0:
    print("Aluno reprovado.")