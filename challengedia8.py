import random
import string

def generar_contraseña():
    longitud = random.randint(8, 16)  # Longitud entre 8 y 16 caracteres, se utiliza la libreria de random
    #para aleatoriedades.   

    # Definir los caracteres a usar
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
#aqui se genera la contraseña tras una eleccion hecha en la libreria con el rango puesto en la longitud
    return contraseña

if __name__ == "__main__":
    contraseña_generada = generar_contraseña()
    print("Su contraseña generada es :", contraseña_generada)
