# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def multiplicacaoPadrao(x, y):
    multiplicador = ""
    multiplicado = ""
    for xx in x:
        multiplicador = multiplicador + str(xx)

    for yy in y:
        multiplicado = multiplicado + str(yy)

    print("   " + multiplicador)
    print("X  " + multiplicado)

    i = len(y)
    resultado_parcial = []
    while i > 0:
        valF = ""
        j = len(x)
        aux = 0
        while j > 0:

            valX = x[j - 1]
            valY = y[i - 1]
            result = (valX * valY)+aux

            if len(str(result)) > 1 and j > 1:
                aux = int(list(str(result))[0])
                valF = list(str(result))[len(list(str(result)))-1] + valF
            else:
                valF = str(result)+valF
                aux = 0;
            j = j-1
        resultado_parcial.append(valF)
        i = i-1

    result_i = 0
    for eqResult in resultado_parcial:
        if result_i > 0:
            zeros = ""
            for x in range(result_i):
                zeros = zeros + "0"
            resultado_parcial[result_i] = eqResult + zeros
        result_i = result_i+1

    resultado = 0
    print("_________________")
    for r in resultado_parcial:
        print(r)
        resultado = resultado + int(r)
    print("_________________")
    print(resultado)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = []
    y = []
    import random
    for i in range(1000):
        x.append(random.randint(0, 9))
        y.append(random.randint(0, 9))

    import time
    inicio = time.time()
    multiplicacaoPadrao(x, y)
    fim = time.time()
    print("\nTempo total do processamento: " + "{:.2f}".format(round(fim - inicio, 2)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
