def nose_repite(palabra):
    lista =  set(palabra)
    for n in palabra:
        lista_nueva = list(lista)
        lista_nueva.sort()
    return print(lista_nueva)        


palabra = ("interacciones")
nose_repite(palabra)
