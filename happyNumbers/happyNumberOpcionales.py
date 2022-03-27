# Opcionales

# a) Modificar el programa para que tanto el valor final al que hay que llegar (1 en el caso de los happy numbers) como la potencia aplicada (2 en el caso de los happy numbers) sean parametrizables. 
# b) Aplicar alguna optimización, suponiendo que la memoria no es problema 


def esHappyNumber(n,visitados, potencia, valFinal):
    if n == valFinal:
        return True
    if n in visitados:
        return False
    visitados[n]= 1
    n = str(n)
    l = list(n)
    l = list(map(int,l))        #arma una lista con la forma lista = {digito1, digito2, digitoN}
    temp = 0
    for i in l:
        temp += (i**potencia)
    return esHappyNumber(temp,visitados, potencia, valFinal)

def imprimirPrimerosHappyNumbers (terminos, pot, valFinal):
    cantHappyNumbers = 0
    num = 1
    while (cantHappyNumbers != terminos):
        if(esHappyNumber(num, {}, pot, valFinal)):
            print(num)
            cantHappyNumbers += 1
        num += 1

terminos = int(input("Ingrese X primeros terminos de happy numbers a calcular "))
pot = int(input("Ingrese una potencia para realizar la suma de potencias "))
valFinal = int(input("Ingrese un valor final para determinar si un numero es happynumber "))

print(f'Los primeros  {terminos} happy numbers son: ')

imprimirPrimerosHappyNumbers(terminos, pot, valFinal)