
package Ejercicio_9;

import java.util.Scanner;

public class Ejercicio_9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite el día: ");
        int dia = entrada.nextInt();
        
        System.out.print("Digite el mes: ");
        int mes = entrada.nextInt();
        
        System.out.print("Digite el año: ");
        int año = entrada.nextInt();
        
        if((dia >= 1 && dia <= 30) && (mes >= 1 && mes <= 12) && (año > 0)) {
            System.out.println("La fecha es correcta.");
        } else {
            System.out.println("La fecha es incorrecta.");
        }
    }
}
