#Hacer un programa que imprima los X primeros “happy numbers”.

def calcularSumaCuadrados(n):
    sumCuadrados = 0
    while(n):
        sumCuadrados += (n % 10) ** 2
        n = int(n / 10)
    return sumCuadrados


def esHappyNumber (n):    
    visitados=set()
    while (1):
        if (n == 1):
            return True
        if n not in visitados:
            visitados.add(n)
            n =  calcularSumaCuadrados(n)
        else:
            return False


def imprimirPrimerosHappyNumbers (terminos):
    cantHappyNumbers = 0
    num = 1
    while (cantHappyNumbers != terminos):
        if(esHappyNumber(num)):
            print(num)
            cantHappyNumbers += 1
        num += 1

terminos = int(input("Ingrese X primeros terminos de happy numbers a calcular "))
print(f'Los primeros  {terminos} happy numbers son: ')
imprimirPrimerosHappyNumbers(terminos)


