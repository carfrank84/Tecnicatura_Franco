/* Ejercicio 7: pedir numeros hasta que se introduzca uno negativo
y calcular la media 
 */
package Ejercicio_7;

import java.util.Scanner;

public class Ejercicio_7 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) { //Mientras el nuemro sea negativo
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo==0){
            System.out.println("\nError, la division entre 0 no existe");
        }
        else{
            promedio = (float)suma/conteo;
            System.out.println("\nEl promedio es : " +promedio);
        }
    }

}
