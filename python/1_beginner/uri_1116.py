
N = int(input())
for n in range(N):
    try:
        X, Y = [int(x) for x in input().split(" ")]
        R = X / Y
        print("{:.1f}".format(R))
    except:
        print("divisao impossivel")
        continue
