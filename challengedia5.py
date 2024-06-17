def crear_diccionario(claves, valores):
    diccionario = dict(zip(claves, valores))
    return diccionario
def main():
    claves_input = input("Ingresa las claves separadas por comas: ")
    valores_input = input("Ingresa los valores separados por comas: ")
    claves = [clave.strip() for clave in claves_input.split(",")]
    valores = [valor.strip() for valor in valores_input.split(",")]
    
    diccionario = crear_diccionario(claves, valores)
    
    print("Diccionario creado:", diccionario)

if __name__ == "__main__":
    main()
