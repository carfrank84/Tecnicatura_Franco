/* Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta que se 
se introduzca un numero negativo
 */
package ciclos01;

import java.util.Scanner;

public class ciclos01 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero, cuadrado;
        System.out.println("Digite un numero:");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) {// mientras el numero sea igual a cero o positivo
            cuadrado = (int) Math.pow(numero, 2);
            System.out.println("El numero  " + numero + "  elevado al cuadrado es :  " + cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());

        }
        System.out.println("El Programa a finalizado por numero negativo");

    }

}

