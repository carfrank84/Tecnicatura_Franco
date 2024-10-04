package clase12Ejercicio2;

import java.util.Scanner;

public class clase12Ejercicio2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el valor de a: ");
        double a = scanner.nextDouble();

        System.out.print("Ingrese el valor de b: ");
        double b = scanner.nextDouble();

        double resultado = Math.pow(a + b, 2);
        double aCuadrado = Math.pow(a, 2);
        double bCuadrado = Math.pow(b, 2);
        double dosAB = 2 * a * b;

        System.out.println("Resultado de (a + b)^2: " + resultado);
        System.out.println("Desglose del calculo:");
        System.out.println("a^2: " + aCuadrado);
        System.out.println("b^2: " + bCuadrado);
        System.out.println("2 * a * b: " + dosAB);
    }
}