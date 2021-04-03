A, B = [int(x) for x in input().split(" ")]

if A > B and A % B == 0:
    print("Sao Multiplos")
elif B > A and B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
