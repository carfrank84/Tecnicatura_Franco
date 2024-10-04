
package calse11Ejercicio2;

import java.util.Scanner;

public class calse11Ejercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double compra, descuento, precio_final;

        System.out.println("Digite la cantidad a pagar:");
        compra = scanner.nextDouble();

        if (compra > 100) {
            descuento = compra * 0.20;
        } else {
            descuento = compra * 0.10;
        }

        precio_final = compra - descuento;

        System.out.println("El precio a pagar es: " + precio_final);
    }
}
 
