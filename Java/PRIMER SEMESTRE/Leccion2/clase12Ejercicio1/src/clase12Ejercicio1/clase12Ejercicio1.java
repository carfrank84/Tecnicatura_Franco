package clase12Ejercicio1;

import java.util.Scanner;

public class clase12Ejercicio1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el numero total de horas: ");
        int totalHoras = scanner.nextInt();

        int semanas = totalHoras / 168; // 1 semana = 168 horas
        int dias = (totalHoras % 168) / 24; // 1 día = 24 horas
        int horas = totalHoras % 24;

        System.out.println("Equivalente a:");
        System.out.println("Semanas: " + semanas);
        System.out.println("Dias: " + dias);
        System.out.println("Horas: " + horas);
    }
}