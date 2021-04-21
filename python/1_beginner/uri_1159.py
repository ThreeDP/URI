import time
import timeit

def test1(i):
    while True:
        i = int(input())
        if i <= 0:
            break
        elif i % 2 == 0:
            print(i + (i + 2) + (i + 4) + (i + 6) + (i + 8))
        else:
            i += 1
            print((i) + (i + 2) + (i + 4) + (i + 6) + (i + 8))

def test2(i):
    while True:
        i = int(input())
        result = 0
        if i <= 0:
            break
        
        elif i % 2 != 0:
            i += 1

        for j in range(0, 10, 2):
            result += i
            i += 2
        print(result)

def test3():
    x = 1
    lista = []
    while x > 0:
        lista.append(int(input()))
        x = lista[-1]
    start = timeit.default_timer()
    for l in lista:
        result = 0
        if l <= 0:
            break
        
        elif l % 2 != 0:
            l += 1

        for j in range(0, 10, 2):
            result += l
            l += 2
        print(result)
    stop = timeit.default_timer()
    print(stop - start)

def test4():
    result = 0
    x = int(input())
    while x != 0:
        if x % 2 != 0:
            x += 1
        
        result = x + (x + 2) + (x + 4) + (x + 6) + (x + 8)
        print(result)
        result = 0
        x = int(input())




#start = timeit.default_timer()
#test3()
#stop = timeit.default_timer()
#print(stop - start)



test4()


'''
start = timeit.default_timer()
test2(n)
stop = timeit.default_timer()
print(stop - start)
'''