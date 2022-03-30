a = -3

if a < 0:
    print(f'{a} es menor que cero')
elif a > 0 :
    print(f'{a} es mayor cero')
else:
    print(f' {a} es igual a cero')


x = 'True'
y  = ''

if type (x) == type(y):
    print ('son el mismo tipo')
else:
    print('son distintos tipos')

for i in range(1, 21):
    if i % 2 == 0:
        print(f'{i} es par')
    else:
        print(f'{i} es impar')

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for i in range(0,6):
    a = i ** 3
    print(f'{i} raised to cube es {a}')

print('5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos')

a = 12
for i in range(0, a):
    print(i)

print('6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, '
      'sólo si la variable contiene un número entero mayor a 0')
a = 3
fact=1
if a > 0:
    for i in range(1, a+1 ):
        fact = fact * i
    print (f'the factorial of {a}  is {fact}')
else:
    print('a es less than zero')

print('7) Crear un ciclo for dentro de un ciclo while')
n=1
while n < 20:
    for n in range(0, 40):
        print(n)
        
        
print('8) Crear un ciclo while dentro de un ciclo for')     
n=25
for i in range (0, 12):
    while n >= 6:
        print(f' n is {n}')
        n -=1
    print (f'i is {i}')

print('Imprimir los números primos existentes entre 0 y 30')
contador = 0
for n in range (0,31):
    primo = True

    for i in range(2, n):
        contador += 1
        if n % i == 0:
            primo = False

           # break
    if primo:
        print(f'{n} es primo')
print (f'contador = {contador}')

print('13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12,'
      ' dentro del rango de números de 100 a 300')

for n in range(100, 301):
    if n % 12 != 0:
        continue
    print(n, 'es divisible por 12')