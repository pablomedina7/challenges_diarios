#include <iostream>

int main() {
    // Declaración de variables
    int num1, num2, suma;

    // Solicitar al usuario el primer número
    std::cout << "Introduce el primer numero: ";
    std::cin >> num1;

    // Solicitar al usuario el segundo número
    std::cout << "Introduce el segundo numero: ";
    std::cin >> num2;

    // Calcular la suma de los dos números
    suma = num1 + num2;

    // Mostrar el resultado de la suma
    std::cout << "La suma de " << num1 << " y " << num2 << " es " << suma << "." << std::endl;

    return 0;
}
