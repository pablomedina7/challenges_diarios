def ordenar_lista(lista):
    return sorted(lista)

def main():
    numeros = input("Ingresa una lista de números separados por comas: ")
    
    lista_numeros = [int(numero.strip()) for numero in numeros.split(",")]
    lista_ordenada = ordenar_lista(lista_numeros)
    
    print("Lista en orden:", lista_ordenada)

if __name__ == "__main__":
    main()
