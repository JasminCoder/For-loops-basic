#Basico: imprime todos los numeros enteros del 0 al 150
for x in range(0, 151):
    print(x)


print("-------")
#Multiplos de 5: imprime todos los multiplos de 5 entre 5 y 1000
for x in range(5, 1001):
    if x % 5 == 0:
        print(x)


print("-------")
#Contar, a la manera Dojo: imprime numeros enteros del 1 al 100. Si es divisible por 5, imprime "Coding"
#en su lugar. Si es divisible por 10, imprime "Coding Dojo"
for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
        continue
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)


print("-------")
#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
sum_impar = 0
for x in range(0, 500000):
    if x % 2 != 0:
        sum_impar += x
print(sum_impar)


print("-------")
#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for x in range(2018, 0, -4): #inicio, final, cantidad a avanzar
    print(x)


print("-------")
#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, 
#imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. 
#El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if (x % mult == 0):
        print(x)