
/*
Ejercicio 3:Leer nuemros hasta que se introduzca un cero
para cada uno indicar si es par o impar.
Primero lo haremos con la calse Scanner
Luego con la calase JOptionPane
 */
package ejercicio_3;

import java.util.Scanner;

public class Ejercicio_3_Scanner {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El numero  " + numero + " es "
                        + "PAR");
            }
            
            else{
                System.out.println("El numero  "+numero+" es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        } 
        System.out.println("El numero ingresado es  "+numero+" finaliza el programa");
    }

}
