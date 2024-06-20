import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]

    while True:
        # Mostrar las opciones disponibles al usuario
        print("\nElije una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        print("4. Salir")
        
        # Obtener la elección del usuario
        eleccion_usuario = input("Ingresa el número de tu elección: ")

        # Validar la entrada del usuario
        if eleccion_usuario == '4':
            print("¡Gracias por jugar!")
            break
        elif eleccion_usuario not in ['1', '2', '3']:
            print("Opción inválida. Por favor ingresa 1, 2, 3, o 4 para salir.")
            continue
        
        # Convertir la elección del usuario a texto
        indice_usuario = int(eleccion_usuario) - 1
        eleccion_usuario = opciones[indice_usuario]

        # Generar elección aleatoria de la computadora
        indice_computadora = random.randint(0, 2)
        eleccion_computadora = opciones[indice_computadora]

        # Mostrar las elecciones
        print(f"\nTu elección: {eleccion_usuario}")
        print(f"Elección de la computadora: {eleccion_computadora}")

        # Determinar el resultado del juego
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        if resultado == "usuario":
            print("¡Ganaste!")
        elif resultado == "computadora":
            print("¡Perdiste!")
        else:
            print("Empate!")

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "empate"
    elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijeras") or \
            (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
            (eleccion_usuario == "tijeras" and eleccion_computadora == "papel"):
        return "usuario"
    else:
        return "computadora"

if __name__ == "__main__":
    jugar_piedra_papel_tijeras()
