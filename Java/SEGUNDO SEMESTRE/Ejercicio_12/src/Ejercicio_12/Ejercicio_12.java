/*
 Ejercicio 12: Pedir un numero y calcular su factorial
hacerlo con las dos clases Scanner y JOptionPane
 */
package Ejercicio_12;
import java.util.Scanner;

public class Ejercicio_12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce un número para calcular su factorial: ");
        int numero = sc.nextInt();
        long factorial = 1;

        for (int i = 1; i <= numero; i++) {
            factorial *= i; // Calcula el factorial
        }

        System.out.println("El factorial de " + numero + " es: " + factorial);
    }
}