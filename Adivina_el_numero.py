from random import randint
su_nombre = input("¿Cual es tu nombre?: ")

while not su_nombre:
     print("Ingrese un nombre valido")
     su_nombre = input("¿Cual es tu nombre?: ")

aleatorio = randint(1,10)

intentos = 8

while intentos > 0:
        elije = int(input(f"{su_nombre} elije un numer del 1 al 10: "))
        if elije > 10:
            print("elije un numero del 1 al 10")
        elif elije < 1:
            print("elije un numero mayor a 0")

        elif aleatorio > elije:
                print(f"Haz elejido un numero menor, intenta de nuevo(tienes {intentos} intentos)")
        elif aleatorio < elije:
            print(f"Haz elejido un numero mayor, intenta de nuevo(tienes {intentos} intentos)")
        elif aleatorio == elije:
            print(f"Feliidades {su_nombre} haz acertado, te a tomado {intentos} intentos")
            break
        intentos -= 1
        if intentos == 0:
            print(f"{su_nombre}Perdiste todas tus vidas :c")
            break