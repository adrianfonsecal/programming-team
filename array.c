#define DIMENSION 5  //Las constantes siempre van al inicio antes del main

// Java verifica límites en los ciclos for, en c puedes declarar un bucle for que verifique más elementos de los que se necesita
#include<stdio.h>

int main(){
    int arreglo[DIMENSION][DIMENSION]; //declarar un vector
    int filas=0, columnas=0; 
   
    for (columnas=0; columnas<DIMENSION; columnas++){
        for (filas=0; filas<DIMENSION; filas++){
            printf("%d, %d\n", filas, columnas); //intercambiar el orden de impresión 
            
        }
        printf("\n");
    }
    return 0;
}
        




    
