#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;
/*esta funcion es para limpiar la cadena*/
string cleanString(const string& str) {
    string cleaned;
    for (char c : str) {
        if (isalnum(c)) {
            cleaned += tolower(c);
        }
    }
    return cleaned;
}
bool isPalindrome(const string& str) {
    string cleaned = cleanString(str);
    int left = 0;
    int right = cleaned.size() - 1;
    
    while (left < right) {
        if (cleaned[left] != cleaned[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}
int main() {
    string input;
    cout << "Ingrese una cadena de caracteres: ";
    getline(cin, input);
    
    if (isPalindrome(input)) {
        cout << "La cadena es un palindromo." << endl;
    } else {
        cout << "La cadena no es un palindromo." << endl;
    }
    return 0;
}
