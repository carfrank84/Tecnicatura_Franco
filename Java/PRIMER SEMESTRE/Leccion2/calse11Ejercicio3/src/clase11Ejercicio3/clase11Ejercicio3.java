
package clase11Ejercicio3;

import java.util.Scanner;

public class clase11Ejercicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num1, num2, resultado;
        boolean sonIguales;

        System.out.println("Ingrese el primer numero:");
        num1 = scanner.nextInt();

        System.out.println("Ingrese el segundo numero:");
        num2 = scanner.nextInt();

        if (num1 == num2) {
            resultado = num1 * num2;
            sonIguales = true;
        } else if (num1 > num2) {
            resultado = num1 - num2;
            sonIguales = false;
        } else {
            resultado = num1 + num2;
            sonIguales = false;
        }

        System.out.println("El resultado es: " + resultado);
        if (sonIguales) {
            System.out.println("Los numeros son iguales y se multiplicaron.");
        } else {
            System.out.println("Los numeros no son iguales.");
        }
    }
}

