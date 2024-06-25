#include <iostream>
using namespace std;
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {22156, 615612634,6562, 255156, 12, 22, 11, 90};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Array original: \n";
    printArray(arr, size);
    
    bubbleSort(arr, size);
    
    cout << "Array ordenado: \n";
    printArray(arr, size);
    
    return 0;
}
