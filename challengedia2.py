#mostrar tabla 
def mostrar_tabla_multiplicar(numero, hasta=10):
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, hasta + 1):
        print(f"{numero} x {i} = {numero * i}")

# ingresar el número
numero_usuario = int(input("ingresa un número: "))

# mostrar el resultado 
mostrar_tabla_multiplicar(numero_usuario)
