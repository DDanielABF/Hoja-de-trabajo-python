def primo():
    n=int(input('Ingrese el numero: '))
    for x in range(2,n):
        if n%x == 0:
            print('El numero no es primo')
            break
        else:
            print('El numero es primo')
            break

primo()