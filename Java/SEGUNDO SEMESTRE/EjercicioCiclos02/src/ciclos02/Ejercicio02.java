/*
 * Ejercicio 2: Leer ubn numero e indicar si es positivo o negativo. El proceso se repetira hasta que se 
introduzca un cero
 */
package ciclos02;

import java.util.Scanner;

public class Ejercicio02 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un Numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero > 0) {
                System.out.println(" El Numero " + numero + " es POSITIVO");
            } else {
                System.out.println("El Numero " + numero + " es NEGATIVO");
            }
            System.out.println("Digite otro Numero:");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El Numero " + numero + " finaliza el programa");

    }

}
