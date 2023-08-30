from random import choice

def lanzar_moneda():
    moneda = ["Cara","Cruz"]
    al_azar = choice(moneda) # elementos al azar en una lista
    return al_azar

def probar_suerte(lista_numeros,lanzar_moneda):
    if lanzar_moneda == "Cara":
        lista_numeros.clear() # borra todos los elemento de la lista
        print("La lista se autodestruirá")
    else:
        print("La lista fue salvada")
        
    return lista_numeros
    

lista_numeros = [5,17,8,8]
moneda_lanzar = lanzar_moneda()
nueva_lista = probar_suerte(lista_numeros, moneda_lanzar)
