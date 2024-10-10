package Ejercicio_10;

/*Ejercicio 10 : Pedir 10 numeros y escribir la suma total
hacerlo con la clase scanner y JOptionPane*/

import java.util.Scanner;

public class Ejercicio_10 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int suma = 0;

        System.out.println("Por favor ingresa 10 números:");

        for (int i = 1; i <= 10; i++) {
            System.out.print("Número " + i + ": ");
            int numero = scanner.nextInt();
            suma += numero;
        }

        System.out.println("La suma total de los números es: " + suma);
    }
}
