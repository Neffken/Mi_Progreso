from random import randint,choice

def asignar_nombre():
   nombre = input("ingrese el nombre del comprador: ")
   return nombre

def asignar_numero(lista_numeros):
   numero = randint(1,5)
   while numero in lista_numeros:
      numero = randint(1,5)
   lista_numeros.append(numero)
   return numero

lista_nombres = []
lista_numeros = []
compradores = 0

while not compradores == 5:
    compradores += 1
    comprador = {f"nombre: {asignar_nombre()}": f"rifa: {asignar_numero(lista_numeros)}"}
    lista_nombres.append(comprador)

ganador = choice(lista_nombres)

print(f"los participantes son: {lista_nombres}")
print(f"el ganador del sorteo es: {ganador}")
