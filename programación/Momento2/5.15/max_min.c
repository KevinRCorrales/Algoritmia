#include "stdio.h"

int main(void){
    int i;
    float numero, max, min;
    i = 1;
    printf("(%d) Ingresa un número:\n", i);
    scanf("%f", &numero);
    max = numero;
    min = numero;
    for (int i = 2; i < 101; i++) {
        printf("(%d) Ingresa un número:\n", i);
        scanf("%f", &numero);
        if (numero > max) {
            max = numero;
        } else {
            if (numero < min) {
                min = numero;
            }
        }
    }
    printf("Máximo %f Minimo %f\n", max, min);
}