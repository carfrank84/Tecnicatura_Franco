package clase12Ejercicio3;

import java.util.Scanner;

public class clase12Ejercicio3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la calificacion de participación: ");
        double participacion = scanner.nextDouble();

        System.out.print("Ingrese la calificacion del primer examen parcial: ");
        double primerParcial = scanner.nextDouble();

        System.out.print("Ingrese la calificacion del segundo examen parcial: ");
        double segundoParcial = scanner.nextDouble();

        System.out.print("Ingrese la calificacion del examen final: ");
        double examenFinal = scanner.nextDouble();

        double calificacionFinal = (participacion * 0.10) +
                                   (primerParcial * 0.25) +
                                   (segundoParcial * 0.25) +
                                   (examenFinal * 0.40);

        System.out.println("La calificacion final es: " + calificacionFinal);
    }
}