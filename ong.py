
def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= n - i
    print(f"El factorial de {n} es {factorial}")

def productoria(lista):
    productoria = 1
    for i in range(len(lista)):
        productoria *= lista[i]
    print(f"La productoria de {lista} es {productoria}")


def calcular(**kwargs):
    for keys,values in kwargs.items():
        if 'fact_' in keys:
            factorial(values)
        elif 'prod_' in keys:
            productoria(values)
        else:
            print("Instruccion mal ingresada")

calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
