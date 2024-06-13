def contador_de_vocales(palabras):
    vocales = 'aeuAEIOU'
    contador = 0
    for caracter in palabras:
        if caracter in vocales:
            contador += 1     
    return contador
palabras = input("ingrese aqui su palabra: ") 
resultado = contador_de_vocales(palabras)
print(f"Número de vocales en la palabra '{palabras}': {resultado}")
